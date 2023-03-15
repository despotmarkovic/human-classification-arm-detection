"""This module provides a PoseDetector class.

It is used for pose estimation (detection) using the Mediapipe library.
Used for human detection and hands above the head detection.
"""

# Import libraries
import cv2
import numpy as np
import mediapipe as mp


class PoseDetector():
    """
    A class for detecting human poses using the MediaPipe library.

    Attributes:
        mode (bool): Which mode will the model
                     run: True for images and False for video
        model_complexity (int): Landmark model complexity
        upBody (bool): Whether to detect the upper body or full body.
        smooth (bool): Whether to apply
                       temporal smoothing to the detected landmarks.
        enable_segmentation (bool): Whether to enable person segmentation.
        detectionCon (float): Detection confidence threshold.
        trackCon (float): Tracking confidence threshold.
    """

    model_complexity = 1
    up_body = False
    smooth = True
    enable_segmentation = False
    track_con = 0.5

    # Initialize the class with default parameters

    def __init__(self, mode=True, detection_con=0.5):
        """Initialize a PoseDetector object with the specified parameters."""
        # Create atributes from passed parameters
        self.mode = mode
        self.detection_con = detection_con

        # Creating instance for pose detection
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(self.mode, self.model_complexity,
                                      self.up_body, self.smooth,
                                      self.enable_segmentation,
                                      self.detection_con,
                                      self.track_con)
        self.results = None

    # Create a method for checking if a human is detected in the image
    def human_check(self, img):
        """
        Detect whether a human is present in the specified image.

        Args:
            img (numpy.ndarray): The image to check.

        Returns:
            int: 1 if a human is detected, 0 otherwise.
        """
        # Convert image to RGB color system
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the image / get detections
        self.results = self.pose.process(img_rgb)

        # If we have detections, there is a human
        if self.results.pose_landmarks:
            return 1
        return 0

    # Create a metod for checking if thw hands are above the head
    def hands_over_head(self, img):
        """
        Detect whether the hands are above the head in the specified image.

        Args:
            img (numpy.ndarray): The image to check.

        Returns:
            int: 1 if both hands are above the head, 0 otherwise.
        """
        # Empty list to store all detected parts of the body
        land_mark_list = []

        if self.results.pose_landmarks:
            landmark_list = self.results.pose_landmarks.landmark
            for i, land_mark in enumerate(landmark_list):

                # Relative coordinates to pixel location in the image
                image_height, image_width, _ = img.shape
                pos_x = int(land_mark.x * image_width)
                pos_y = int(land_mark.y * image_height)
                land_mark_list.append([i, pos_x, pos_y])

            # Sumarize points of interest on head, left and right hand
            head_avg = np.round(
                np.mean(land_mark_list[0:11], axis=0))[1:3]
            right_hand = np.round(
                np.mean(land_mark_list[16:24:2], axis=0))[1:3]
            left_hand = np.round(
                np.mean(land_mark_list[15:23:2], axis=0))[1:3]

            # If both hands have lower x value, they are closer to the top
            if (left_hand[1] < head_avg[1] and right_hand[1] < head_avg[1]):
                return 1
            return 0

        return 0
