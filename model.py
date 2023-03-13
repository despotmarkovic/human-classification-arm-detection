# Import libraries
import cv2
import numpy as np
import mediapipe as mp
import time
import os
import pickle

# Create a class for pose estimation (detection)
class PoseDetector():
    
    # Initialize the class with default parameters
    def __init__(self, mode = True, model_complexity = 1, upBody = False,
                 smooth = True, enable_segmentation = False, detectionCon = 0.5,
                 trackCon = 0.5):
        
        # Create atributes from passed parameters
        self.mode = mode
        self.model_complexity = model_complexity
        self.upBody = upBody
        self.smooth = smooth
        self.enable_segmentation = enable_segmentation
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        # Creating instance for pose detection
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.model_complexity, self.upBody,
                                    self.smooth, self.enable_segmentation, self.detectionCon,
                                     self.trackCon)
    
    # Create a method for checking if a human is detected in the image
    def HumanCheck(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR image format to RGB image format
        self.results = self.pose.process(imgRGB) # Process the image / get detections
        
        # If we have detections, there is a human
        if (self.results.pose_landmarks):
            return 1
        else:
            return 0
    
    # Create a metod for checking if thw hands are above the head
    def HandsOverHead(self, img):
        lmlist = [] # Empty list to store all detected parts of the body
        
        if (self.results.pose_landmarks):
            for id, lm in enumerate(self.results.pose_landmarks.landmark): # Going through all detected pairs
                
                # Converting relative coordinates to exact pixel location in the image    
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
            
            # Sumarizing points of interest that belongs to head, left and right hand
            head_avg = np.round(np.mean(lmlist[0:11], axis = 0))[1:3]
            right_hand = np.round(np.mean(lmlist[16:24:2], axis = 0))[1:3]
            left_hand = np.round(np.mean(lmlist[15:23:2], axis = 0))[1:3]
            
            # If both hands have lower x value, they are closer to the top of the image
            if(left_hand[1] < head_avg[1] and right_hand[1] < head_avg[1]):
                return 1
            else:
                return 0
            
        return 0

    
