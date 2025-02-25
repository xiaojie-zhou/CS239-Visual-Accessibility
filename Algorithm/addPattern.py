import cv2
import numpy as np

# Load the barplot image
img = cv2.imread('barplot.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary image (tweak parameters as needed)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Detect contours which should correspond to the bars
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Calculate the area of each contour's bounding box and find the maximum area
areas = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    areas.append(w * h)
max_area = max(areas) if areas else 0

# Set a relative threshold (e.g., 10% of the maximum area)
relative_threshold = 0.1 * max_area

# Process each detected contour using the relative area filter
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = w * h
    if area < relative_threshold:
        continue  # Skip small regions

    # Extract the bar region
    bar_region = img[y:y+h, x:x+w]

    # (Optional) Determine the average color of the bar
    avg_color = cv2.mean(bar_region)[:3]

    # Create a blank image for the pattern (same size as the bar region)
    pattern = np.zeros_like(bar_region)

    # Draw a simple diagonal line pattern on the pattern image
    step = 10  # Adjust spacing for the pattern
    for i in range(-w, h, step):
        pt1 = (max(i, 0), max(-i, 0))
        pt2 = (min(w + i, w), min(h - i, h))
        cv2.line(pattern, pt1, pt2, (0, 0, 0), 1)

    # Blend the pattern with the original bar region (adjust alpha values as needed)
    blended = cv2.addWeighted(bar_region, 0.7, pattern, 0.3, 0)
    img[y:y+h, x:x+w] = blended

cv2.imshow('Barplot with Patterns', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
