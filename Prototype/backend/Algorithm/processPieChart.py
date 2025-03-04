import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import euclidean
import os

import cv2
import numpy as np
import os
import math

def sample_line_color(img, center, angle, radius, num_samples=50):
    """
    Sample the color along a line from the center to the edge at a given angle.
    :param img: Input image (RGB)
    :param center: (x, y) coordinates of the pie chart center
    :param angle: Angle in degrees (0-360)
    :param radius: Length of the sampling line
    :param num_samples: Number of points to sample along the line
    :return: Average color along the line
    """
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)  # Convert to radians

    # Sample points along the line
    colors = []
    for i in range(num_samples):
        r = (i / num_samples) * radius  # Progressively extend from center to radius
        x = int(x_center + r * np.cos(angle_rad))
        y = int(y_center + r * np.sin(angle_rad))

        # Get pixel color (handle out-of-bounds cases)
        if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
            colors.append(img[y, x])  # OpenCV uses (y, x)

    # Compute average color (mean R, G, B)
    avg_color = np.mean(colors, axis=0)
    return tuple(map(int, avg_color))


def detect_pie_slices(img, center, radius, threshold=30):
    """
    Detect pie chart slices by sampling colors along radial lines and tracking color changes.
    :param img: Input image (RGB)
    :param center: (x, y) center of the pie chart
    :param radius: Radius of the pie chart
    :param threshold: Color difference threshold to detect region changes
    :return: List of (start_angle, end_angle, color) tuples
    """
    angle_regions = []
    prev_color = sample_line_color(img, center, 0, radius)
    start_angle = 0

    for angle in range(1, 361):  # Iterate over 360 degrees
        current_color = sample_line_color(img, center, angle, radius)

        # Compute Euclidean color difference
        color_diff = np.linalg.norm(np.array(prev_color) - np.array(current_color))

        if color_diff > threshold:  # Detect a new region
            angle_regions.append((start_angle, angle - 1, prev_color))
            start_angle = angle
            prev_color = current_color

    # Handle 359° to 0° connection
    first_region_color = angle_regions[0][2]
    last_region_color = angle_regions[-1][2]
    if np.linalg.norm(np.array(first_region_color) - np.array(last_region_color)) < threshold:
        # Merge first and last regions
        angle_regions[0] = (angle_regions[-1][0], angle_regions[0][1], first_region_color)
        angle_regions.pop()

    return angle_regions


def recolor_pie_chart(input_path, output_folder, color_palette=None):
    """
    Detects and recolors pie chart segments using radial color sampling.
    """
    # Load image
    file_name = os.path.splitext(os.path.basename(input_path))[0]
    img = cv2.imread(input_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert to grayscale for circle detection
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # Step 1: Detect the Pie Chart (find circular contour)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the most circular contour (assume it's the pie chart)
    round_contours = sorted(contours, key=lambda c: cv2.arcLength(c, True) / (cv2.contourArea(c) + 1e-5), reverse=False)
    (x, y), radius = cv2.minEnclosingCircle(round_contours[0])
    center = (int(x), int(y))
    radius = int(radius)

    # Step 2: Detect Pie Slices
    angle_regions = detect_pie_slices(img_rgb, center, radius)

    # Step 3: Assign Colors & Apply Overlays
    overlay = img_rgb.copy()
        # reference: https://davidmathlogic.com/colorblind
    acadia_color_palettes = {
    'normal': ['#FED789', '#023743', '#72874E', '#476F84', '#A4BED5', '#453947'],
    'prot': ['#332288', '#117733', '#44AA99', '#88CCEE', '#DDCC77', '#CC6677', '#AA4499', '#882255', '#661100'],
    'deut': ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000'],
    'trit': ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7'],
    'gray': ['#000000', '#666666', '#999999', '#CCCCCC', '#DDDDDD', '#EEEEEE']
    }
    color_palette = acadia_color_palettes['normal']


    for i, (start_angle, end_angle, _) in enumerate(angle_regions):
        new_color = color_palette[i % len(color_palette)]
        new_color = tuple(int(new_color[i:i+2], 16) for i in (1, 3, 5))

        # Draw filled slices
        for angle in range(start_angle, end_angle + 1):
            angle_rad = np.deg2rad(angle)
            x1 = int(center[0] + radius * np.cos(angle_rad))
            y1 = int(center[1] + radius * np.sin(angle_rad))
            cv2.line(overlay, center, (x1, y1), new_color, thickness=2)

    # Step 4: Save Output
    output_path = os.path.join(output_folder, f"{file_name}_recolored.png")
    cv2.imwrite(output_path, cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR))

    print(f"Saved output to {output_path}")



if __name__ == '__main__':
    # Usage
    recolor_pie_chart('./Prototype/backend/Algorithm/piechart_raw.png', 
                        './Prototype/backend/Algorithm/')
