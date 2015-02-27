FROM resin/rpi-raspbian:latest
RUN apt-get update
RUN apt-get install -y python python-pip python-dev python-dbus
RUN apt-get install -y dropbear
RUN apt-get install -y net-tools usbutils
RUN apt-get install -y hostapd udhcpd
COPY . /app
CMD ["bash", "/app/start.sh"]
