import numpy as np
import matplotlib.pyplot as plt
import colorsys

# Function to map hex color to grayscale using logarithmic scaling and hue adjustment
def hex_to_gray(hex_color_str):
    r = int(hex_color_str[0:2], 16)
    g = int(hex_color_str[2:4], 16)
    b = int(hex_color_str[4:6], 16)
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)

    # Standard luminance formula
    y = 0.299 * r + 0.587 * g + 0.114 * b

    # Adjust based on hue (adds small variation)
    adjusted_gray = round(min(255, max(0, y + 80 * h)))

    return "#{:02X}{:02X}{:02X}".format(adjusted_gray, adjusted_gray, adjusted_gray)

if __name__ == "__main__":

    # Example Hex Colors
    hex_colors = ["D81B60", "2674B9", "0000ff", "ff00ff", "00ffff", "ffff00", "808080"]

    # Convert to grayscale values in HEX format
    gray_values = [hex_to_gray(color) for color in hex_colors]

    # Convert grayscale HEX back to RGB tuples for visualization
    gray_rgb_colors = [tuple(int(v[i:i+2], 16) for i in (1, 3, 5)) for v in gray_values]

    # Create an image with color blocks
    block_size = 100  # Size of each color block
    image_height = block_size * len(hex_colors)
    image_width = block_size * 2  # Original and grayscale side by side

    # Create an empty image
    image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

    # Populate the image with color blocks
    for i, (hex_color, gray_color) in enumerate(zip(hex_colors, gray_rgb_colors)):
        # Convert hex to RGB
        rgb = tuple(int(hex_color[j:j + 2], 16) for j in (0, 2, 4))

        # Fill the left side with original color
        image[i * block_size:(i + 1) * block_size, :block_size] = rgb

        # Fill the right side with grayscale equivalent
        image[i * block_size:(i + 1) * block_size, block_size:] = gray_color

    # Display the image
    plt.figure(figsize=(5, len(hex_colors)))
    plt.imshow(image)
    plt.axis("off")  # Hide axes
    plt.show()