# Importing required modules
import cv2
import os
from flask import Flask, jsonify, request, render_template, abort
import numpy as np
import model

# Initialize Flask app
app = Flask(__name__)

# Instantiate the pose detection model
model = model.PoseDetector()

# Define image extensions
image_ext = {'png', 'jpg', 'jpeg'}

# Function to check if file is an image with a valid extension
def check_file(filename):
    return ((('.' in filename) and (filename.rsplit('.', 1)[1]) in image_ext))

# Route for the home page
@app.route('/',methods = ['GET'])
def front():
    # Render the front-end template with empty values for the detected human and hands over head classification
    return render_template('front.html', human_detection = '',hands_classification ='')

# Route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Check if the file is an image and has a valid extension
    if('image' not in request.files.keys()) or (check_file(request.files['image'].filename) == False): # Comment while testing
        abort(400, 'Bad file type! Choose file with .png, .jpg or .jpeg extension! ') # Comment while testing 
    
    # Read the image file from the request and decode it using OpenCV
    image_file = request.files['image']
    image_file = np.fromfile(image_file, np.uint8)
    image = cv2.imdecode(image_file, cv2.IMREAD_COLOR)
    
    # Detect if there is a human in the image and classify whether the person has their hands over their head
    human_detection = model.HumanCheck(image)
    hands_classification = model.HandsOverHead(image)
    
    # Render the front-end template with the detected human and hands over head classification
    return render_template('front.html',human_detection=human_detection,hands_classification=hands_classification )

if __name__ == '__main__':
    # Run the Flask app on the specified port or the default 5000
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))