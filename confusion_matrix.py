"""This module calculates 2 confusion matrices.

One for human detection and second for hands above the head.
"""
# Importing required modules
import os
import random
import numpy as np
import cv2
import model


# Defining the main function
def main():
    """Loop through all folders to calculate confusion matrices."""
    # Creating an instance of the PoseDetector class
    detector = model.PoseDetector()

    # Defining the paths to the three image directories
    class0_path = "./testimages/0/"
    class1_path = "./testimages/1/"
    class2_path = "./testimages/2/"

    # Creating two confusion matrices for evaluation
    confmat_detection = np.zeros([2, 2])
    confmat_hands_detection = np.zeros([2, 2])

    # Looping over all files in the first image directory
    for file_name in os.listdir(class0_path):
        # Reading the image file and checking for human presence
        img = cv2.imread(class0_path + file_name)
        human_detected = detector.human_check(img)

        # Updating the confusion matrix for human detection
        confmat_detection[human_detected, int(file_name[0])] += 1

    # Looping over all files in the second image directory
    for file_name in os.listdir(class1_path):
        # Reading the image file and checking for human and hands above head
        img = cv2.imread(class1_path + file_name)
        human_detected = detector.human_check(img)
        hands_above = detector.hands_over_head(img)

        # Updating the confusion matrices
        confmat_detection[human_detected, int(file_name[0])] += 1
        confmat_hands_detection[hands_above, int(file_name[0])-1] += 1

    # Looping over all files in the third image directory
    for file_name in os.listdir(class2_path):
        # Reading the image file and checking for human and hands above head
        img = cv2.imread(class2_path + file_name)
        human_detected = detector.human_check(img)
        hands_above = detector.hands_over_head(img)

        # Updating the confusion matrices
        confmat_detection[human_detected, int(file_name[0])-1] += 1
        confmat_hands_detection[hands_above, int(file_name[0])-1] += 1

    # Printing the confusion matrices
    print(f"Confusion Matrix"
          f"for human detection:\n{confmat_detection}\n")
    print(f"Confusion Matrix"
          f"for hands up detection:\n{confmat_hands_detection}")


# Running the main function if this file is executed directly
if __name__ == '__main__':
    random.seed(123)
    main()
