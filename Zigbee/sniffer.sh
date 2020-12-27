#!/bin/sh

echo [*] Start Whsniff
sudo whsniff -c 16 > out.pcap &
echo [*] Sleep 1 min
sleep 300
echo [*] kill whsniff

sudo killall whsniff
echo [*] write sniffer

/home/kali/RadioSecurity/Zigbee/sniffer.py
