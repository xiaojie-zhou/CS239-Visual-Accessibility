import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import euclidean
import os

def add_hatches_to_bars(input_path, output_folder, hatch_alpha=0.3, change_color=True, color_palette='normal_vision'):
    """
    Adjust colors and add hatch patterns to bars in a bar plot image.
    :param input_path: Path to the input image
    :param output_folder: Path to the output folder
    :param hatch_alpha: Alpha value for blending the hatches with the original image
    :param change_color: If True, the bars will be colored with a predefined color palette
    :param color_palette: choose from ['normal', 'prot', 'deut', 'trit', 'gray']

    Results:
    - hatched_bars.png: The image with hatched patterns on the bars
    - color_adjusted.png: The original image with color adjustments (only when change_color=True)
    """
    # Load image and convert color spaces

    # Get the filename w/o extension
    file_name_with_ext = os.path.basename(input_path)
    file_name_without_ext = os.path.splitext(file_name_with_ext)[0]

    img = cv2.imread(input_path)
    # get the image size
    height, width, _ = img.shape
    print(height, width)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    original = img_rgb.copy()
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    
    # Step 1: Detect plot area using edge detection
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest rectangular contour (plot area)
    plot_contour = max(contours, key=lambda cnt: cv2.contourArea(cv2.convexHull(cnt)))
    x, y, w, h = cv2.boundingRect(plot_contour)

    # Crop to plot area
    margin = 10  # Add some margin
    x, y, w, h = x + margin, y + margin, w - 2*margin, h - 2*margin
    plot_area = gray[y:y+h, x:x+w]
    
    # Step 2: Detect bars within plot area
    # Adaptive thresholding for better bar detection
    thresh = cv2.adaptiveThreshold(plot_area, 255, 
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY_INV, 11, 2)
    
    # Morphological operations to clean up
    kernel = np.ones((1,1), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    # Find bar contours
    bar_contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # # DRAW ALL contours
    # cv2.drawContours(plot_area, bar_contours, -1, (0, 255, 0), 2)
    # cv2.imshow('All Contours', cv2.cvtColor(plot_area, cv2.COLOR_RGB2BGR))
    # cv2.imwrite('contours.png', cv2.cvtColor(plot_area, cv2.COLOR_RGB2BGR))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Filter and collect bars with coordinates in the original image space
    bars = []
    legends = []
    min_bar_area = 100  # Adjust based on image size
    for cnt in bar_contours:
        area = cv2.contourArea(cnt)
        if area < min_bar_area:
            continue
        xb, yb, wb, hb = cv2.boundingRect(cnt)
        xb += x
        yb += y
        aspect_ratio = wb / float(hb)
        if aspect_ratio > 1.5: # most likely a legend
            legends.append((xb, yb, wb, hb))
            continue
        # detect bars based on color variance
        roi = img_rgb[yb:yb+hb, xb:xb+wb]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)
        h_variance = np.var(hsv_roi[:, :, 0])
        s_variance = np.var(hsv_roi[:, :, 1])
        v_variance = np.var(hsv_roi[:, :, 2])
        if h_variance < 100 and s_variance < 100 and v_variance < 100:
            bars.append((xb, yb, wb, hb + 7))
    
    x_legend, y_legend, w_legend, h_legend = legends[0]
    margin_legend = 5
    x_legend, y_legend, w_legend, h_legend = x_legend + margin_legend, y_legend + margin_legend, w_legend - 2*margin_legend, h_legend - 2*margin_legend
    legend_area = gray[y_legend:y_legend+h_legend, x_legend:x_legend+w_legend]

    # Adaptive thresholding for better bar detection
    thresh = cv2.adaptiveThreshold(legend_area, 255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 5, 2)

    # Morphological operations to clean up
    kernel = np.ones((1, 1), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    # Find bar contours
    legend_contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter and collect bars with coordinates in the original image space
    legend_bars = []
    min_bar_area = 5 # Adjust based on image size
    small_bar_margin = 0
    for cnt in legend_contours:
        area = cv2.contourArea(cnt)
        if area < min_bar_area:
            continue
        xb, yb, wb, hb = cv2.boundingRect(cnt)
        xb = legends[0][0] + xb + margin_legend
        yb = legends[0][1] + yb + margin_legend
        roi = img_rgb[yb:yb+hb, xb:xb+wb]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)
        h_variance = np.var(hsv_roi[:, :, 0])
        s_variance = np.var(hsv_roi[:, :, 1])
        v_variance = np.var(hsv_roi[:, :, 2])
        if h_variance < 100 and s_variance < 100 and v_variance < 100:
            legend_bars.append((xb + small_bar_margin, yb + small_bar_margin, wb -2*small_bar_margin, hb -2*small_bar_margin))


    bars = bars + legend_bars
    # # plot the bars
    # for (xb, yb, wb, hb) in bars:
    #     cv2.rectangle(img_rgb, (xb, yb), (xb + wb, yb + hb), (0, 0, 255), 2)
    # cv2.imshow('All Bars', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
    # # save the image
    # cv2.imwrite('bars.png', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # Step 3: Extract and cluster bar colors
    bar_colors = []
    for (xb, yb, wb, hb) in bars:
        roi = original[yb:yb+hb, xb:xb+wb]
        roi_hsv = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)
        avg_color = np.mean(roi_hsv.reshape(-1, 3), axis=0)
        bar_colors.append(avg_color)
    bar_colors = np.array(bar_colors)
    print(bar_colors)

    dbscan = DBSCAN(eps=10, min_samples=2, metric=lambda a, b: euclidean(a, b))
    labels = dbscan.fit_predict(bar_colors)
    print(labels)
    
    group_bars = {}
    for i, label in enumerate(labels):
        if label not in group_bars:
            group_bars[label] = []
        group_bars[label].append(bars[i])

    # Create a color map that maps the label to the corresponding color
    color_map = {}
    for label in np.unique(labels):
        if label == -1:
            continue  # Skip noise points
        # Get the average color of the bars in this cluster
        cluster_colors = bar_colors[labels == label]
        avg_color = np.mean(cluster_colors, axis=0)
        color_map[label] = cv2.cvtColor(np.uint8([[avg_color]]), cv2.COLOR_HSV2RGB)[0][0]
    print(color_map)
    
    # # visualize the grouped bars
    # for group, bar_list in group_bars.items():
    #     print(f'Group {group}: {len(bar_list)} bars')
    #     color = tuple(np.random.randint(0, 255, 3).tolist())  # Random color for each group
    #     for (x, y, w, h) in bar_list:
    #         cv2.rectangle(img_rgb, (x, y), (x + w, y + h), color, 2)
    # cv2.imshow('Grouped Bars', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # reference: https://davidmathlogic.com/colorblind
    acadia_color_palettes = {
    'normal': ['#FED789', '#023743', '#72874E', '#476F84', '#A4BED5', '#453947'],
    'prot': ['#332288', '#117733', '#44AA99', '#88CCEE', '#DDCC77', '#CC6677', '#AA4499', '#882255', '#661100'],
    'deut': ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000'],
    'trit': ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7'],
    'gray': ['#000000', '#666666', '#999999', '#CCCCCC', '#DDDDDD', '#EEEEEE']
    }
    acadia_color_palette = acadia_color_palettes[color_palette]


    # Step 4: Create hatch patterns
    patterns = [
        {'type': 'horizontal', 'spacing': 8, 'thickness': 2},
        {'type': 'vertical', 'spacing': 8, 'thickness': 2},
        {'type': 'diagonal', 'spacing': 13, 'thickness': 2, 'slope': 1},
        {'type': 'cross', 'spacing': 8, 'thickness': 2},
        {'type': 'dots', 'spacing': 12, 'radius': 2}
    ]
    
    # Create overlay
    color_overlay = original.copy()
    hatch_overlay = np.zeros_like(original, dtype=np.uint8) # for hatches
    for i, (group, bar_list) in enumerate(group_bars.items()):
        if change_color:
            bar_color = acadia_color_palette[i % len(acadia_color_palette)]
            bar_color = tuple(int(bar_color[i:i+2], 16) for i in (1, 3, 5))
            for (xb, yb, wb, hb) in bar_list:
                cv2.rectangle(color_overlay, (xb, yb), (xb+wb, yb+hb), bar_color, -1)
    # Save the result with color adjustments
    result = color_overlay.copy()
    output_path = os.path.join(output_folder, file_name_without_ext+'_color_adjusted.png')
    cv2.imwrite(output_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))

    if change_color:
        hatch_overlay = color_overlay.copy()
    else:
        hatch_overlay = original.copy()
    for i, (group, bar_list) in enumerate(group_bars.items()):
        pattern = patterns[i % len(patterns)]
        bar_color = color_map[group]
        # get the luminance of the color and if it is less than 128, use white hatches
        luminance = 0.299 * bar_color[0] + 0.587 * bar_color[1] + 0.114 * bar_color[2]
        print(luminance)
        color = (255, 255, 255) if luminance < 128 else (0, 0, 0)  # White if dark, black if bright

        for (xb, yb, wb, hb) in bar_list:
            if pattern['type'] == 'horizontal':
                for y_line in range(yb, yb+hb+1, pattern['spacing']):
                    cv2.line(hatch_overlay, (xb + 1, y_line), (xb+wb-1, y_line), color, pattern['thickness'])
            elif pattern['type'] == 'vertical':
                for x_line in range(xb, xb+wb+1, pattern['spacing']):
                    cv2.line(hatch_overlay, (x_line, yb+1), (x_line, yb+hb), color, pattern['thickness'])
            elif pattern['type'] == 'cross':
                for y_line in range(yb, yb+hb, pattern['spacing']):
                    cv2.line(hatch_overlay, (xb, y_line), (xb+wb, y_line), color, pattern['thickness'])
                for x_line in range(xb, xb+wb, pattern['spacing']):
                    cv2.line(hatch_overlay, (x_line, yb), (x_line, yb+hb), color, pattern['thickness'])
            elif pattern['type'] == 'dots':
                for y_dot in range(yb, yb+hb, pattern['spacing']):
                    for x_dot in range(xb, xb+wb, pattern['spacing']):
                        cv2.circle(hatch_overlay, (x_dot, y_dot), pattern['radius'], color, -1)
            elif pattern['type'] == 'diagonal':
                step = pattern['spacing']
                k = pattern['slope']
                # Top-left to bottom-right diagonals
                x_start = xb + wb - step
                wb -= 1
                while True:
                    if x_start < xb:
                        break
                    pt1 = (x_start, yb + hb)
                    pt2_y = yb + hb - (xb + wb - x_start) * k
                    if pt2_y < yb:
                        pt2_x = x_start + hb / k
                        pt2 = (int(pt2_x), yb)
                    else:
                        pt2 = (xb + wb, int(pt2_y))
                    cv2.line(hatch_overlay, pt1, pt2, color, pattern['thickness'])
                    x_start -= step

                y_start = yb + hb
                while True:
                    if y_start < yb:
                        break        
                    pt1 = (xb, y_start)
                    pt_2_y = y_start - k * wb
                    if pt_2_y < yb:
                        pt2_x = 2 * xb - (yb + k * xb - y_start)
                        pt2 = (int(pt2_x), yb)
                    else:
                        pt2 = (xb + wb, int(pt_2_y))
                    cv2.line(hatch_overlay, pt1, pt2, color, pattern['thickness'])
                    y_start -= step
                
            #
            # # show the current bar contour and hatch pattern
            # cv2.rectangle(overlay, (xb, yb), (xb+wb, yb+hb), (255, 0, 0), 2)
            # cv2.imshow('Bar Contour with Hatch Pattern', cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR))
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
    
    # Blend and save
    result = cv2.addWeighted(hatch_overlay, 1 - hatch_alpha, hatch_overlay, hatch_alpha, 0)
    output_path = os.path.join(output_folder, file_name_without_ext+'_hatched_bars.png')
    cv2.imwrite(output_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))

if __name__ == '__main__':
    # Usage
    add_hatches_to_bars('./Prototype/backend/Algorithm/barplot_raw.png', 
                        './Prototype/backend/Algorithm/', hatch_alpha=0.5, change_color=True, color_palette='normal_vision')
