import scipy.io
import os
import pandas as pd
from process_mat import load_mat_files

def mat_data_to_csv(data, output_csv_path):

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Write to .csv file
    df.to_csv(output_csv_path, index=False)
    print(f"Processed: variable {var_name} -> {output_csv_path}")


root_directory = (r'/home/goto/Dumpyard/archive')

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
        # Convert to .csv file
        mat_data_to_csv(data, os.path.splitext(mat_path)[0] + '.csv')
    else:
        print(f"No  variable found in {mat_path}")

