
# Download and launch the project

Developing a Computer Vision model that will get as an input a picture and output whether there is a person or not and whether the hands are above the head or not.

Developing API to facilitate integration, enable innovation, increase automation and scalability usnig Flask library. 

Dockerfile and docker image

Testing with pytest library

Developed and tested on Windows 10



## Download and Run

To download and run the application, follow the steps.

1. Create a folder and navigate the working directory to the created folder where you want do download the content. In terminal/PowerShell type:
```bash
  cd path/to/directory
```
2. Download the content from the git repository:
```bash
git clone https://github.com/despotmarkovic/human-classification-arm-detection.git
```

3. Navigate from current directory to downloaded directory:
```bash
cd human-classification-arm-detection
```

4. Depending on operating system, download and intialize the appropriate Docker for your local machine:

Link: https://www.docker.com/products/docker-desktop/

5. Build a docker image by running the next command in terminal/PowerShell:
```bash
docker build -t image_name -f Dockerfile ./
```

6. Run the Docker container by running the next command:
```bash
docker run -d --name container_name -p 80:5000 image_name
```
Check if the container is running:
```bash
docker ps
```
Check which IP address to use to run the app:
```bash
docker logs container_name
```





## Testing using test_api.py script

Open new terminal/PowerShell. Run the test_api.py script with pytest library:
```bash
pytest test_api.py
```

In test_api.py script, you can change the path to the image or file you want to run the test with.

