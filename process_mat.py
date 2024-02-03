import os

def load_mat_files(root_directory):
    mat_files = []
    
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.mat'):
                mat_path = os.path.join(root, file)
                mat_files.append(mat_path)
    
    print("\n".join(mat_files),)

    return mat_files


load_mat_files(r'E:\College\2nd year\Inter Disciplinary\Rice False smut\WHY-HI')
