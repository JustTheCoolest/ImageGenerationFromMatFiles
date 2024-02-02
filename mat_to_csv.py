import scipy.io
import pandas as pd

# Load the .mat file
mat = scipy.io.loadmat('/home/goto/Dumpyard/Test25.mat')

# Extract the data
data = mat['Test25']  # replace 'name_of_variable' with your variable name

# Convert to DataFrame
df = pd.DataFrame(data)

# Write to .csv file
df.to_csv('file.csv', index=False)