# Requirement: pip install daltonlens
from daltonlens import convert, simulate, generate
import PIL
import numpy as np
import os


def simulate_colorblind(image_path, output_folder, severity=1, save=True):
    """
    Simulate color blindness effects on an image and save results in a specified folder.

    :param image_path: Path to the input image
    :param severity: Severity level of color vision deficiency (default=1)
    :param save: If True, save the output images
    :param output_folder: Folder where the output images will be saved (default="simulation")
    :return: Dictionary containing the simulated images
    """

    # Load image
    image = np.asarray(PIL.Image.open(image_path).convert('RGB'))

    # Create a simulator using the Viénot 1999 algorithm.
    simulator = simulate.Simulator_Brettel1997()

    # Apply the simulator to generate different types of colorblind simulations
    filtered_images = {}
    for deficiency in [simulate.Deficiency.PROTAN, simulate.Deficiency.DEUTAN, simulate.Deficiency.TRITAN]:
        filtered_images[deficiency.name] = simulator.simulate_cvd(image, deficiency=deficiency, severity=severity)

    # Save the filtered images in the specified output folder
    if save:
        base_filename = os.path.splitext(os.path.basename(image_path))[0]  # Extract filename without extension
        for deficiency, filtered in filtered_images.items():
            save_path = os.path.join(output_folder, f"{base_filename}_{deficiency}.png")
            PIL.Image.fromarray(filtered).save(save_path)
            print(f"Saved: {save_path}")

    return filtered_images


def simulate_colorblind_multiple_input(image_list, severity=1):
    all_filtered_images = []
    for image in image_list:
        # Apply the simulator to the input image to get a simulation of protanomaly
        filtered_images = simulate_colorblind(image, severity, save=False)
        all_filtered_images.append(filtered_images)
    # show all figures in a len(imag_list) x 3 grid
    from matplotlib import pyplot as plt
    fig, axs = plt.subplots(len(image_list), 4, figsize=(12, 4*len(image_list)))
    for i, image_path in enumerate(image_list):
        # Show the original image in the leftmost column
        original_image = np.asarray(PIL.Image.open(image_path).convert('RGB'))
        axs[i, 0].imshow(original_image)
        axs[i, 0].set_title('Original')
        axs[i, 0].axis('off')
        
        # Show the simulated images in the remaining columns
        filtered_images = all_filtered_images[i]
        for j, (deficiency, filtered) in enumerate(filtered_images.items(), start=1):
            axs[i, j].imshow(filtered)
            axs[i, j].set_title(deficiency)
            axs[i, j].axis('off')
    plt.tight_layout()
    plt.show()
    return all_filtered_images

    return filtered_images

if __name__ == '__main__':
    simulate_colorblind('/Users/XiaojieZhou/UCLA/CS239/CS239-Visual-Accessibility/Prototype/backend/Algorithm/barplot_raw.png', "/Users/XiaojieZhou/UCLA/CS239/CS239-Visual-Accessibility/Prototype/backend/simulation")
    # image_list = ['Prototype/backend/Algorithm/barplot_raw.png',
    #               'Prototype/backend/Algorithm/color_adjusted.png',
    #               'Prototype/backend/Algorithm/hatched_bars.png']
    # simulate_colorblind_multiple_input(image_list, 1)