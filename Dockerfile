FROM python:3.9.0

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get update && apt-get install -y nano

CMD ["python", "rest_api.py"]