#!/bin/bash
#Set the root password as root if not set as an ENV variable
export PASSWD=${PASSWD:=root}
#Set the root password
echo "root:$PASSWD" | chpasswd
modprobe snd-bcm2835
#Spawn dropbear
dropbear -E -F-s &
#start your application from here...
python app/server.py
