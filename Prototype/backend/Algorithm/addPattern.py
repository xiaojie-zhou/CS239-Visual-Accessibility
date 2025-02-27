import cv2
import numpy as np
from sklearn.cluster import KMeans

def add_hatches_to_bars(input_path, output_path, num_colors=3, hatch_alpha=0.3):
    # Load image and convert color spaces
    img = cv2.imread(input_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    original = img_rgb.copy()
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    
    # Step 1: Detect plot area using edge detection
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest rectangular contour (plot area)
    plot_contour = max(contours, key=lambda cnt: cv2.contourArea(cv2.convexHull(cnt)))
    x, y, w, h = cv2.boundingRect(plot_contour)

    # # show the contour
    # cv2.drawContours(img_rgb, [plot_contour], -1, (0, 255, 0), 2)
    # cv2.imshow('Contour', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # Crop to plot area
    margin = 10  # Add some margin
    x, y, w, h = x + margin, y + margin, w - 2*margin, h - 2*margin
    plot_area = gray[y:y+h, x:x+w]
    plot_area_rgb = img_rgb[y:y+h, x:x+w]
    
    # Step 2: Detect bars within plot area
    # Adaptive thresholding for better bar detection
    thresh = cv2.adaptiveThreshold(plot_area, 255, 
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY_INV, 11, 2)
    
    # Morphological operations to clean up
    kernel = np.ones((3,3), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    # Find bar contours
    bar_contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # # show the bar contours
    # cv2.drawContours(plot_area_rgb, bar_contours, -1, (0, 255, 0), 2)
    # cv2.imshow('Bar Contours', cv2.cvtColor(plot_area_rgb, cv2.COLOR_RGB2BGR))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # Filter and collect bars
    bars = []
    min_bar_area = 100  # Adjust based on image size
    for cnt in bar_contours:
        area = cv2.contourArea(cnt)
        xb, yb, wb, hb = cv2.boundingRect(cnt)
        aspect_ratio = wb / float(hb)
        
        # Basic bar characteristics (adjust as needed)
        if area > min_bar_area and aspect_ratio < 0.8:
            # Convert coordinates back to original image space
            bars.append((x + xb, y + yb, wb, hb))
    
    # Step 3: Extract and cluster bar colors
    bar_colors = []
    for (xb, yb, wb, hb) in bars:
        roi = img_rgb[yb:yb+hb, xb:xb+wb]
        avg_color = np.mean(roi, axis=(0, 1))
        bar_colors.append(avg_color)
    print(bar_colors)
    kmeans = KMeans(n_clusters=num_colors, n_init=10, random_state=42)
    labels = kmeans.fit_predict(bar_colors)
    print(labels)

    # Step 4: Create hatch patterns
    patterns = [
        {'type': 'horizontal', 'spacing': 8, 'thickness': 2},
        {'type': 'vertical', 'spacing': 8, 'thickness': 2},
        {'type': 'diagonal', 'spacing': 8, 'thickness': 2, 'slope': 1},
        {'type': 'cross', 'spacing': 8, 'thickness': 2},
        {'type': 'dots', 'spacing': 12, 'radius': 2}
    ]
    
    # Create overlay
    overlay = original.copy()
    for i, (xb, yb, wb, hb) in enumerate(bars):
        pattern = patterns[labels[i] % len(patterns)]
        color = (0, 0, 0)  # Black hatches
        if pattern['type'] == 'horizontal':
            for y_line in range(yb, yb+hb, pattern['spacing']):
                cv2.line(overlay, (xb, y_line), (xb+wb, y_line), color, pattern['thickness'])
        elif pattern['type'] == 'vertical':
            for x_line in range(xb, xb+wb, pattern['spacing']):
                cv2.line(overlay, (x_line, yb), (x_line, yb+hb), color, pattern['thickness'])
        elif pattern['type'] == 'cross':
            for y_line in range(yb, yb+hb, pattern['spacing']):
                cv2.line(overlay, (xb, y_line), (xb+wb, y_line), color, pattern['thickness'])
            for x_line in range(xb, xb+wb, pattern['spacing']):
                cv2.line(overlay, (x_line, yb), (x_line, yb+hb), color, pattern['thickness'])
        elif pattern['type'] == 'dots':
            for y_dot in range(yb, yb+hb, pattern['spacing']):
                for x_dot in range(xb, xb+wb, pattern['spacing']):
                    cv2.circle(overlay, (x_dot, y_dot), pattern['radius'], color, -1)
        elif pattern['type'] == 'diagonal':
            step = pattern['spacing']
            k = pattern['slope']
            # Top-left to bottom-right diagonals
            x_start = xb + wb - step

            while True:
                if x_start < xb:
                    break
                pt1 = (x_start, yb + hb)
                pt2_y = yb + hb - (xb + wb - x_start) * k
                if pt2_y < yb:
                    pt2_x = x_start + hb / k
                    pt2 = (pt2_x, yb)
                else:
                    pt2 = (xb + wb, pt2_y)
                cv2.line(overlay, pt1, pt2, color, pattern['thickness'])
                x_start -= step

            y_start = yb + hb
            while True:
                if y_start < yb:
                    break        
                pt1 = (xb, y_start)
                pt_2_y = y_start - k * wb
                if pt_2_y < yb:
                    pt2_x = 2 * xb - (yb + k * xb - y_start)
                    pt2 = (pt2_x, yb)
                else:
                    pt2 = (xb + wb, pt_2_y)
                cv2.line(overlay, pt1, pt2, color, pattern['thickness'])
                y_start -= step
            
        
        # show the current bar contour and hatch pattern
        cv2.rectangle(overlay, (xb, yb), (xb+wb, yb+hb), (255, 0, 0), 2)
        cv2.imshow('Bar Contour with Hatch Pattern', cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # Blend and save
    result = cv2.addWeighted(original, 1 - hatch_alpha, overlay, hatch_alpha, 0)
    cv2.imwrite(output_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))

# Usage
add_hatches_to_bars('barplot.png', 'output.png', num_colors=5, hatch_alpha=0.4)