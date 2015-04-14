FROM resin/rpi-raspbian:latest
RUN apt-get update && apt-get install -y \
python python-pip python-dev python-dbus python-flask python-pycurl \
alsa-base alsa-utils libasound2-dev mplayer \
dropbear \
&& apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install twilio
COPY . /app
CMD ["bash", "/app/start.sh"]
