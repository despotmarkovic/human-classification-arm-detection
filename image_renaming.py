import os

# Locations of folders on local machine (0, 1 and 2 - changeable parameter)
dir_path = "C://Users//Despot Markovic//Desktop//Incode - Project//Software//testimages//2"
files = os.listdir(dir_path)

# Loop throug all files in the folder
for i, file_name in enumerate(files):
    file_ext = os.path.splitext(file_name)[1] # Take the file extension
    new_file_name = f"{2}_{i}{file_ext}" # Generate new file name
    
    old_path = os.path.join(dir_path, file_name) # Old path
    new_path = os.path.join(dir_path, new_file_name) #New path
    
    os.rename(old_path, new_path) #Renaming the file