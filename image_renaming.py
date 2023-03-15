"""This module is used to rename images.

It renames the image to start with 0, 1 or 2, depending on the class.
"""
# Importing required modules
import os


def image_rename(directory_list):
    """
    Loop through all folders and rename the images.

    Attributes:
        dir_list: List of directories to loop through
    """
    for dir_path in directory_list:
        files = os.listdir(dir_path)

        # Loop throug all files in the folder
        for i, file_name in enumerate(files):

            # Take the file extension
            file_ext = os.path.splitext(file_name)[1]

            # Generate new file name
            new_file_name = f"{dir_path[-1]}_{i}{file_ext}"

            # Old path
            old_path = os.path.join(dir_path, file_name)

            # New path
            new_path = os.path.join(dir_path, new_file_name)

            # Renaming the file
            os.rename(old_path, new_path)


if __name__ == '__main__':
    dir_list = ['./testimages/0', './testimages/1',
                './testimages/2']
    image_rename(dir_list)
