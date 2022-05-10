FROM python:3.9-slim
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
CMD exec gunicorn run:server --bind :$PORT