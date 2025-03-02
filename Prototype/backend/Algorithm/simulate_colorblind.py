# Requirement: pip install daltonlens
from daltonlens import convert, simulate, generate
import PIL
import numpy as np

def simulate_colorblind(image_path, severity=1, save=True):
    # Generate a test image that spans the RGB range
    image = np.asarray(PIL.Image.open(image_path).convert('RGB'))

    # Create a simulator using the Viénot 1999 algorithm.
    simulator = simulate.Simulator_Brettel1997()

    # Apply the simulator to the input image to get simulations of protanomaly, deuteranomaly, and tritanomaly
    filtered_images = {}
    for deficiency in [simulate.Deficiency.PROTAN, simulate.Deficiency.DEUTAN, simulate.Deficiency.TRITAN]:
        filtered_images[deficiency.name] = simulator.simulate_cvd(image, deficiency=deficiency, severity=severity)
    
    # save the filtered image
    if save:
        for deficiency, filtered in filtered_images.items():
            save_path = image_path.split('.')[0] + '_' + deficiency + '.png'
            PIL.Image.fromarray(filtered).save(save_path)
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
    simulate_colorblind('Prototype/backend/Algorithm/barplot_raw.png', 1)
    image_list = ['Prototype/backend/Algorithm/barplot_raw.png', 
                  'Prototype/backend/Algorithm/color_adjusted.png',
                  'Prototype/backend/Algorithm/hatched_bars.png']
    simulate_colorblind_multiple_input(image_list, 1)