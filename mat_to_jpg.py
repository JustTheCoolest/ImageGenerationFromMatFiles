import scipy.io
import matplotlib.pyplot as plt

# Load .mat file
mat = scipy.io.loadmat('/home/goto/Dumpyard/Test25.mat')

# Extract data
data = mat['Test25']

# Save as .jpg
plt.imsave('output.jpg', data, cmap='gray')