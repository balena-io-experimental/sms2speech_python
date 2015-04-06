FROM resin/rpi-raspbian:latest
RUN apt-get update
RUN apt-get install -y python python-pip python-dev python-dbus python-flask python-pycurl alsa-utils mplayer
RUN apt-get install -y dropbear
RUN pip install twilio
RUN pip install pycurl
COPY . /app
CMD ["bash", "/app/start.sh"]
