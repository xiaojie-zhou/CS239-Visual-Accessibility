import cv2
import numpy as np
from skimage.color import rgb2gray
from sklearn.cluster import MiniBatchKMeans
from daltonlens import simulate
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from concurrent.futures import ThreadPoolExecutor


### 🚀 UTILITY FUNCTIONS ###
def resize_image(image, max_size=512):
    """Downscale image for faster processing while retaining visual features."""
    h, w, _ = image.shape
    scale = max_size / max(h, w)
    return cv2.resize(image, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA) if scale < 1 else image


def extract_dominant_colors(image, k=5):
    """Extract k dominant colors using MiniBatchKMeans (fast)."""
    image_resized = resize_image(image)
    pixels = image_resized.reshape(-1, 3)

    kmeans = MiniBatchKMeans(n_clusters=k, n_init=3, batch_size=500, random_state=42)
    kmeans.fit(pixels)
    return kmeans.cluster_centers_.astype(int)


### 🚀 1️⃣ COLOR BLIND SIMULATION & SCORE ###
def simulate_color_blindness(image):
    """Simulate color blindness (deuteranopia)."""
    simulator = simulate.Simulator_Vienot1999()
    return simulator.simulate_cvd(resize_image(image, max_size=200), deficiency=simulate.Deficiency.DEUTAN, severity=1.0)


def get_color_blindness_score(image, colors):
    """Measure color distinction after color blindness simulation."""
    simulated = simulate_color_blindness(image)
    cb_colors = extract_dominant_colors(simulated, k=len(colors))

    # Convert to LAB space (faster calculations)
    lab_colors = np.array([convert_color(sRGBColor(*c / 255.0), LabColor) for c in cb_colors])
    lab_values = np.array([[c.lab_l, c.lab_a, c.lab_b] for c in lab_colors])

    # Compute distances in LAB space
    color_diffs = np.linalg.norm(lab_values[:, None] - lab_values, axis=-1)
    mean_distance = np.mean(color_diffs[np.triu_indices(len(colors), 1)])

    return 10 if mean_distance > 50 else 8 if mean_distance > 35 else 6 if mean_distance > 20 else 4 if mean_distance > 10 else 2


### 🚀 2️⃣ GRAYSCALE READABILITY SCORE ###
def get_grayscale_score(gray_image):
    """Measure grayscale contrast (higher = better readability)."""
    contrast = gray_image.std()
    return 10 if contrast > 50 else 7 if contrast > 30 else 4 if contrast > 15 else 0


### 🚀 3️⃣ PATTERN DETECTION SCORE ###
def detect_patterns(image):
    """Detects patterns using edge detection."""
    edges = cv2.Canny(image, 50, 150)
    edge_density = np.sum(edges > 0) / edges.size
    return 10 if edge_density > 0.1 else 7 if edge_density > 0.05 else 4 if edge_density > 0.02 else 0


### 🚀 4️⃣ FINAL ACCESSIBILITY SCORE (WITHOUT CONTRAST) ###
def evaluate_image(image_path):
    """Compute final accessibility score of a chart/graph (No contrast score)."""
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB once
    gray_image = rgb2gray(image_rgb) * 255  # Convert to grayscale once

    colors = extract_dominant_colors(image_rgb)

    # Parallelize tasks for speed
    with ThreadPoolExecutor(max_workers=3) as executor:
        cb_future = executor.submit(get_color_blindness_score, image_rgb, colors)
        grayscale_future = executor.submit(get_grayscale_score, gray_image)
        pattern_future = executor.submit(detect_patterns, image)

        cb_score = cb_future.result() * 4
        grayscale_score = grayscale_future.result() * 3
        pattern_score = pattern_future.result() * 3

    total_score = cb_score + grayscale_score + pattern_score
    return round(total_score, 2)


### 🚀 RUN IMAGE EVALUATION ###
if __name__ == '__main__':
    image_path = "/Users/XiaojieZhou/UCLA/CS239/CS239-Visual-Accessibility/Prototype/backend/Algorithm/test/barplot_raw.png"
    score = evaluate_image(image_path)
    print(f"📊 Image Accessibility Score: {score}/100")