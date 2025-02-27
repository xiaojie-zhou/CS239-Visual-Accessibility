from daltonlens import convert, simulate, generate
import PIL
import numpy as np

# Generate a test image that spans the RGB range
im = np.asarray(PIL.Image.open("barplot.png").convert('RGB'))

# Create a simulator using the Viénot 1999 algorithm.
simulator = simulate.Simulator_Vienot1999()

# Apply the simulator to the input image to get a simulation of protanomaly
protan_im = simulator.simulate_cvd (im, simulate.Deficiency.PROTAN, severity=1.0)

# show the image
PIL.Image.fromarray(protan_im).show()