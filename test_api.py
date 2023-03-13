# Importing required modules
import requests
import cv2
import pytest

# Defining a fixture to retrieve the API URL
@pytest.fixture
def api_url():
    return 'http://127.0.0.1:5000'
    
# Testing GET request
def test_get(api_url):
    response = requests.get(f'{api_url}/')
    assert response.status_code == 200

# Testing POST request
def test_post(api_url):
    # Defining the image path and request parameter key
    image_path = 'C:/Users/Despot Markovic/Desktop/Incode - Project/Software_html/testimages/1/1_144.png'
    request_param = 'image'
    
    # Reading the image file and encoding it
    image = cv2.imread(image_path)
    
    assert image is not None , "No such image on that location!"
    
    _, img_encoded = cv2.imencode('.jpg', image)
    
    # Making a POST request to the API endpoint
    assert request_param =='image' , "Bad request key parameter!"
    
    response = requests.post(f'{api_url}/predict', files={request_param : img_encoded})
    
    # Asserting the status code of the response
    assert response.status_code==200
        