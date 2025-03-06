import cv2
import numpy as np
from skimage.color import rgb2gray
from sklearn.cluster import KMeans
from daltonlens import simulate

def relative_luminance(rgb):
    """ Computes the relative luminance of an RGB color (0-255 scale) """
    def channel_luminance(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * channel_luminance(r) + 0.7152 * channel_luminance(g) + 0.0722 * channel_luminance(b)

def contrast_ratio(color1, color2):
    """ Computes contrast ratio between two colors based on WCAG 2.1 """
    lum1 = relative_luminance(color1)
    lum2 = relative_luminance(color2)

    L1, L2 = max(lum1, lum2), min(lum1, lum2)
    return (L1 + 0.05) / (L2 + 0.05)

def get_contrast_score(colors, background=(255, 255, 255)):
    """ Computes contrast score using WCAG guidelines """
    scores = []
    for color in colors:
        ratio = contrast_ratio(color, background)
        if ratio >= 7:
            scores.append(10)
        elif ratio >= 4.5:
            scores.append(7)
        elif ratio >= 3:
            scores.append(4)
        else:
            scores.append(0)
    return np.mean(scores) * 4  # Weighted 40%

def extract_dominant_colors(image_path, k=5):
    """ Extracts the k most dominant colors from an image using k-means clustering """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    pixels = image.reshape(-1, 3)

    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)

    return colors


def simulate_color_blindness(image_path, deficiency='deuteranopia'):
    """ Uses daltonlens to simulate color blindness """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

    # Map deficiency string to daltonlens Deficiency
    deficiency_mapping = {
        'protanopia': simulate.Deficiency.PROTAN,
        'deuteranopia': simulate.Deficiency.DEUTAN,
        'tritanopia': simulate.Deficiency.TRITAN
    }
    deficiency_type = deficiency_mapping.get(deficiency.lower(), simulate.Deficiency.DEUTAN)

    # Create a simulator instance (e.g., using Viénot 1999 algorithm)
    simulator = simulate.Simulator_Vienot1999()

    # Apply the simulator to the input image
    simulated_image = simulator.simulate_cvd(image, deficiency=deficiency_type, severity=1.0)
    return simulated_image

def get_color_blindness_score(image_path):
    """ Checks if the graph remains distinguishable under color blindness """
    image = cv2.imread(image_path)
    simulated = simulate_color_blindness(image_path, 'deuteranopia')  # Options: 'deuteranopia', 'protanopia', 'tritanopia'

    diff = np.abs(image.astype(float) - simulated.astype(float)).mean()
    if diff > 40:
        return 10
    elif diff > 30:
        return 7
    elif diff > 20:
        return 4
    else:
        return 0  # Poor differentiation

def get_grayscale_score(image_path):
    """ Evaluates how distinguishable a graph is in grayscale """
    image = cv2.imread(image_path)
    gray = rgb2gray(image) * 255  # Convert to grayscale

    contrast = gray.std()  # Standard deviation measures contrast in grayscale
    if contrast > 50:
        return 10
    elif contrast > 30:
        return 7
    elif contrast > 15:
        return 4
    else:
        return 0  # Poor grayscale readability

def detect_patterns(image_path):
    """ Tries to detect if patterns, markers, or varied line styles are used """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 100, 200)  # Detect edges

    edge_density = np.sum(edges > 0) / edges.size  # Measure pattern complexity
    if edge_density > 0.1:
        return 10  # Likely patterns exist
    elif edge_density > 0.05:
        return 7
    elif edge_density > 0.02:
        return 4
    else:
        return 0  # Likely just solid colors

def evaluate_graph(image_path):
    """ Computes the final accessibility score of the PNG graph """
    colors = extract_dominant_colors(image_path)

    contrast_score = get_contrast_score(colors)
    cb_score = get_color_blindness_score(image_path) * 3  # 30% weight
    grayscale_score = get_grayscale_score(image_path) * 2  # 20% weight
    pattern_score = detect_patterns(image_path)  # 10% weight

    total_score = contrast_score + cb_score + grayscale_score + pattern_score
    return round(total_score, 2)

if __name__ == '__main__':
    image_path = "/Users/XiaojieZhou/UCLA/CS239/CS239-Visual-Accessibility/Prototype/backend/Algorithm/barplot_raw.png"  # Replace with the actual path to your PNG graph
    score = evaluate_graph(image_path)
    print(f"📊 Graph Accessibility Score: {score}/100")