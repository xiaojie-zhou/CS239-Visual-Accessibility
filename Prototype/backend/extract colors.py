import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Function to extract dominant colors from an image
def extract_colors(image_path, num_colors=5, resize_factor=0.25):
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return []

    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is successfully loaded
    if image is None:
        print("Error: Image not found or unable to load.")
        return []

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (0, 0), fx=resize_factor, fy=resize_factor)

    # Reshape into a 2D array of pixels
    pixels = image.reshape((-1, 3))

    # Apply K-means clustering to find dominant colors
    kmeans = KMeans(n_clusters=num_colors, random_state=0, n_init=10)
    kmeans.fit(pixels)

    # Get the cluster centers (dominant colors)
    dominant_colors = np.round(kmeans.cluster_centers_).astype(int)

    return dominant_colors

if __name__ == "__main__":

    # Example: Extract colors from an image
    image_path = "user_input/20250227130339.png"  # Update with correct path
    num_colors = 5  # Number of dominant colors to detect

    dominant_colors = extract_colors(image_path, num_colors)

    if dominant_colors.any():
        # Convert to hex for visualization
        hex_colors = ["#{:02X}{:02X}{:02X}".format(*color) for color in dominant_colors]

        # Plot the extracted colors
        fig, ax = plt.subplots(1, num_colors, figsize=(10, 2))
        for i, color in enumerate(dominant_colors):
            ax[i].imshow([[color / 255]])  # Normalize for display
            ax[i].set_title(hex_colors[i], fontsize=10)
            ax[i].axis("off")

        plt.show()