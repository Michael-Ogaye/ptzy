FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev \
    libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev \
    libjpeg-dev libfreetype6-dev \
    apt-get install -y --no-install-recommends \
    python-pygame 
    

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "game.py"]
