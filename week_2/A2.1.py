# Assignment #2: Task #1 

# importing os module 
import os 

# Get the list of all files and directories in the root directory 
path ="C:\\Users\Lenovo\Documents\GitHub\Python-Bootcamp-DSC-DSU\week_1"
dir_list = os.listdir(path) 

print("Files and directories in '", path, "' :") 

# print the list 
print(dir_list) 

# Printing the list by loop
# for x in dir_list:
#     print(x)


def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("C:\\Users\Lenovo\Documents\GitHub\Python-Bootcamp-DSC-DSU\week_1")
