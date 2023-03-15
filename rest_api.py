"""
This module creates API communication (POST request).

Create API request, process it and returns the predictions in JSON format.
"""
# Importing required modules
import os
import cv2
from flask import Flask, jsonify, request, abort, make_response
import numpy as np
import model

# Initialize Flask app
app = Flask(__name__)

# Instantiate the pose detection model
model = model.PoseDetector()


# Route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    """
    Check and process API POST request.

    Returns:
        {'contains_person': human_detection,
         'hands_above_head':hands_classification}
    """
    # Check if the file is an image and has a valid extension
    if 'image' not in request.files.keys() or \
            'name' not in request.form.keys():
        abort(make_response(jsonify(message="Bad request!"), 400))

    # Check if the file is an image and has a valid extension
    if request.form['name'].endswith(('.jpg', '.png', '.jpeg')) is False:
        abort(make_response(jsonify(message="Bad file type!"), 400))

    # Read the image file from the request and decode it using OpenCV
    image_file = request.files['image']
    image_file = np.fromfile(image_file, np.uint8)
    image = cv2.imdecode(image_file, cv2.IMREAD_COLOR)

    # Detect if there is a human on the image
    human_detection = model.human_check(image)

    # Detect if hands are above the head
    hands_classification = model.hands_over_head(image)

    # Return a JSON file as a response
    return jsonify({'contains_person': human_detection,
                    'hands_above_head': hands_classification})


if __name__ == '__main__':
    # Run the Flask app on the specified port or the default 5000
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
