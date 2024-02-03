import scipy.io
import os
import matplotlib.pyplot as plt
from process_mat import load_mat_files

root_directory = (r'E:\College\2nd year\Inter Disciplinary\Rice False smut\WHY-HI')

# loading all the .mat files
mat_files = load_mat_files(root_directory)

for mat_path in mat_files:
    # Load .mat file
    mat = scipy.io.loadmat(mat_path)
    var_names = list(mat.keys())

    # Check if  variable names matches 'test'
    matching_var_names = [var_name for var_name in var_names if 'train' in var_name.lower() or 'test' in var_name.lower()]

    if matching_var_names:
        var_name = matching_var_names[-1]  
        print(f"Variable names : {var_name}")
        print("path of the variable file : ", mat_path)

        # Extract data
        data = mat[var_name]

       

        # Write to .csv file
      
        output_jpg_path = os.path.splitext(mat_path)[0] + '.jpg'
        plt.imsave(output_jpg_path, data, cmap='gray')
        print(f"Processed: {mat_path} -> {output_jpg_path}")
    else:
        print(f"No  variable found in {mat_path}")    