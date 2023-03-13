# Importing required modules
import cv2
import os
import model
import numpy as np
import random

# Defining the main function
def main():
    # Creating an instance of the PoseDetector class
    detector = model.PoseDetector()
    
    # Defining the paths to the three image directories
    class0_path="C:/Users/Despot Markovic/Desktop/Incode - Project/Software/testimages/0/"
    class1_path="C:/Users/Despot Markovic/Desktop/Incode - Project/Software/testimages/1/"
    class2_path="C:/Users/Despot Markovic/Desktop/Incode - Project/Software/testimages/2/"
    
    # Creating two confusion matrices for evaluation
    confmat_detection = np.zeros([2, 2])
    confmat_hands_detection = np.zeros([2, 2])
    
    # Looping over all files in the first image directory
    for file_name in os.listdir(class0_path):
        # Reading the image file and checking for human presence
        img = cv2.imread(class0_path + file_name)
        human_detected = detector.HumanCheck(img)
        
        # Updating the confusion matrix for human detection
        confmat_detection[human_detected, int(file_name[0])]+=1
     
    # Looping over all files in the second image directory
    for file_name in os.listdir(class1_path):
        # Reading the image file and checking for human and hands above head
        img = cv2.imread(class1_path + file_name)
        human_detected = detector.HumanCheck(img)
        hands_above = detector.HandsOverHead(img)
        
        # Updating the confusion matrices for human detection and hands above head detection
        confmat_detection[human_detected, int(file_name[0])]+=1
        confmat_hands_detection[hands_above, int(file_name[0])-1]+=1

    # Looping over all files in the third image directory
    for file_name in os.listdir(class2_path):
        # Reading the image file and checking for human and hands above head
        img = cv2.imread(class2_path + file_name)
        human_detected = detector.HumanCheck(img)
        hands_above = detector.HandsOverHead(img)
        
        # Updating the confusion matrices for human detection and hands above head detection
        confmat_detection[human_detected, int(file_name[0])-1]+=1
        confmat_hands_detection[hands_above, int(file_name[0])-1]+=1

    # Printing the confusion matrices 
    print(f'Confusion Matrix for numan detection:\n{confmat_detection}\n')
    print(f'Confusion Matrix for hands up detection:\n{confmat_hands_detection}')
 
# Running the main function if this file is executed directly
if __name__ =='__main__':
    random.seed(123)
    main()

    
    
        
