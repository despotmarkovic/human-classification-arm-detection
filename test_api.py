"""
This module creates API test cases and runs using pytest library.

Create different test casses with all possible input situations.
"""
import os
import requests
import cv2


# Person detected and hands above the head test case
def test_hands_above_head():
    """
    Create test for image containing a person with hands above the head.
    """
    image_path = './testimages/2/2_52.jpg'
    img_name = os.path.basename(image_path)

    image = cv2.imread(image_path)

    _, img_encoded = cv2.imencode('.jpg', image)

    # Make a request to the API with the test image
    response = requests.post('http://localhost:5000/predict',
                             files={'image': img_encoded},
                             data={'name': img_name},
                             timeout=15)
    # Verify the response
    assert response.ok
    assert response.json() == {'contains_person': 1, 'hands_above_head': 1}


# Person detected and hands below the head test case
def test_hands_down():
    """
    Create test for image containing a person with hands below the head.
    """
    image_path = './testimages/1/1_54.png'
    img_name = os.path.basename(image_path)

    image = cv2.imread(image_path)

    _, img_encoded = cv2.imencode('.jpg', image)

    # Make a request to the API with the test image
    response = requests.post('http://localhost:5000/predict',
                             files={'image': img_encoded},
                             data={'name': img_name},
                             timeout=15)

    # Verify the response
    assert response.ok
    assert response.json() == {'contains_person': 1, 'hands_above_head': 0}


# Test if the API returns expected output when given an image with no person
def test_no_person():
    """
    Create test for image without a person.
    """
    image_path = './testimages/0/0_59.png'
    img_name = os.path.basename(image_path)

    image = cv2.imread(image_path)

    _, img_encoded = cv2.imencode('.jpg', image)

    # Make a request to the API with the test image
    response = requests.post('http://localhost:5000/predict',
                             files={'image': img_encoded},
                             data={'name': img_name},
                             timeout=15)

    # Verify the response
    assert response.ok
    assert response.json() == {'contains_person': 0, 'hands_above_head': 0}


# Test if the API returns an error when given an invalid file type
def test_bad_file_type():
    """
    Create test for file which isn't a good type.'
    """
    file_path = './testimages/test_text.txt'
    file_name = os.path.basename(file_path)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Make a request to the API with the test image
    response = requests.post('http://localhost:5000/predict',
                             files={'image': file_data},
                             data={'name': file_name},
                             timeout=15)

    # Verify the response
    assert response.status_code == 400
    assert response.json() == {'message': 'Bad file type!'}


# Test if the API returns an error when given an invalid request
def test_bad_request_name():
    """
    Create test for bad request inputs.
    """
    image_path = './testimages/0/0_288.jpg'
    image_name = os.path.basename(image_path)

    image = cv2.imread(image_path)

    _, img_encoded = cv2.imencode('.jpg', image)

    # Make a request to the API with the test image
    response = requests.post('http://localhost:5000/predict',
                             files={'noimage': img_encoded},
                             data={'name': image_name},
                             timeout=15)

    # Verify the response
    assert response.status_code == 400
    assert response.json() == {'message': 'Bad request!'}


# Test if the API returns an error when given a non-existent file
def test_nonexistent_file():
    """
    Create test for loading nonexisting files.
    """
    image_path = './testimages/nonexistingimage.png'
    image_name = os.path.basename(image_path)
    image = cv2.imread(image_path)

    # Make a request to the API with a non-existent file
    response = requests.post('http://localhost:5000/predict',
                             files={'image': image},
                             data={'name': image_name},
                             timeout=15)

    # Verify the response
    assert response.status_code == 400
