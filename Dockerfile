FROM resin/rpi-raspbian:latest
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python python-pip python-dev python-dbus python-flask python-pycurl alsa-base alsa-utils libasound2-dev mplayer
RUN apt-get install -y dropbear
RUN pip install twilio
COPY . /app
CMD ["bash", "/app/start.sh"]
