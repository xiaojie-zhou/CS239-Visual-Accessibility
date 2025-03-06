import cv2
import numpy as np
from skimage.color import rgb2gray
from sklearn.cluster import KMeans
from daltonlens import simulate


def extract_dominant_colors_from_image(image, k=5):
    """ 使用 K-Means 聚类提取图像中的 k 个主要颜色 """
    pixels = image.reshape(-1, 3)  # 重新调整形状，使其成为 RGB 值列表

    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)  # K-Means 聚类
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)  # 获取聚类中心（主色）
    return colors

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

def get_contrast_score(colors):
    """ 计算图表内所有主要颜色之间的对比度 """
    contrast_values = []

    for i in range(len(colors)):
        for j in range(i + 1, len(colors)):  # 计算所有颜色组合的对比度
            ratio = contrast_ratio(colors[i], colors[j])
            contrast_values.append(ratio)

    if not contrast_values:
        return 0  # 避免空列表错误

    avg_contrast = np.mean(contrast_values)  # 计算所有对比度的平均值

    # WCAG 标准评分
    if avg_contrast >= 7:
        return 10
    elif avg_contrast >= 4.5:
        return 7
    elif avg_contrast >= 3:
        return 4
    else:
        return 2  # 不设为 0，避免过度惩罚亮色

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
    """ 直接评估色盲用户是否能区分颜色，而不是和原图比 """
    image = cv2.imread(image_path)
    simulated = simulate_color_blindness(image_path, 'deuteranopia')

    # 提取色盲模拟图像的主色调
    colors = extract_dominant_colors_from_image(simulated, k=5)  # 提取 5 种主色
    color_distances = []

    # 计算所有颜色之间的欧几里得距离，判断它们的区分度
    for i in range(len(colors)):
        for j in range(i + 1, len(colors)):
            dist = np.linalg.norm(colors[i] - colors[j])  # 计算颜色向量之间的距离
            color_distances.append(dist)

    # 计算颜色差异的平均值
    mean_distance = np.mean(color_distances) if color_distances else 0

    # 根据颜色差异分配评分
    if mean_distance > 100:  # 颜色明显不同
        return 10
    elif mean_distance > 75:
        return 8
    elif mean_distance > 50:
        return 6
    elif mean_distance > 30:
        return 4
    else:
        return 2  # 颜色几乎相同，难以区分

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

    contrast_score = get_contrast_score(colors) * 4
    cb_score = get_color_blindness_score(image_path) * 3  # 30% weight
    grayscale_score = get_grayscale_score(image_path) * 2  # 20% weight
    pattern_score = detect_patterns(image_path)  # 10% weight
    print(contrast_score, cb_score, grayscale_score, pattern_score)

    total_score = contrast_score + cb_score + grayscale_score + pattern_score
    return round(total_score, 2)

if __name__ == '__main__':
    image_path = "/Users/XiaojieZhou/UCLA/CS239/CS239-Visual-Accessibility/Prototype/backend/Algorithm/hatched_bars.png"
    score = evaluate_graph(image_path)
    print(f"📊 Graph Accessibility Score: {score}/100")