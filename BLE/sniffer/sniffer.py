#!/usr/bin/python

from __future__ import absolute_import
from __future__ import print_function
from six.moves import input
__author__ = "ktown"
__copyright__ = "Copyright Adafruit Industries 2014 (adafruit.com)"
__license__ = "MIT"
__version__ = "0.1.0"

import os
import sys
import time
import argparse
import csv
import requests
import mysql.connector as mariadb 
from datetime import datetime
from SnifferAPI import Logger
from SnifferAPI import Sniffer
from SnifferAPI import CaptureFiles
from SnifferAPI.Devices import Device
from SnifferAPI.Devices import DeviceList


mySniffer = None
"""@type: SnifferAPI.Sniffer.Sniffer"""


def setup(serport, delay=6):
    """
    Tries to connect to and initialize the sniffer using the specific serial port
    @param serport: The name of the serial port to connect to ("COM14", "/dev/tty.usbmodem1412311", etc.)
    @type serport: str
    @param delay: Time to wait for the UART connection to be established (in seconds)
    @param delay: int
    """
    global mySniffer

    # Initialize the device on the specified serial port
    print("Connecting to sniffer on " + serport)
    mySniffer = Sniffer.Sniffer(serport)
    # Start the sniffer
    mySniffer.start()
    # Wait a bit for the connection to initialise
    time.sleep(delay)


def scanForDevices(scantime=5):
    print("Starting BLE device scan ({0} seconds)".format(str(scantime)))

    mySniffer.scan()
    time.sleep(scantime)
    devs = mySniffer.getDevices()
    devstr = str(devs)
    devlist=devstr.split("BLE")
    del devlist[0] #Delete Description
    for i in devlist:
        name=str(i).split('""',1)[1].split('""',1)[0]
        values=str(i).split("[",1)[1].split("]",1)[0]
        valuelist=values.split(",")
        newlist=[]
        for i in valuelist:
            i=i.replace(' ','')
            try:
                x=hex(int(i)).replace('0x','')
            except:
                x=i
            if len(x)==1: # Wenn ein Teil der MAC einstellig ist, fuehrende '0' anstellen
                x='0'+ x
            newlist.append(x)
        mac = newlist[0] + ':' +newlist[1] + ':' + newlist[2] + ':' + newlist[3] + ':' + newlist[4] + ':' + newlist[5]
        connectable = newlist[6]
        print(newlist[6])
        time.sleep(2)
        if newlist[6] == 'False':
            r = requests.get('https://api.macvendors.com/' + mac);
            vendor = r.text
        else:
            vendor = 'Not found'
        if vendor.find('errors') == -1:
            vendor = vendor
        else:
            vendor ='Not found'
        device=[name,mac,connectable,vendor]
       
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print("Error connecting to MariaDB: " + e)
        
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ble(name, mac, connect, vendor, last_seen) VALUES ('"+ name + "', '" + mac + "', '" + connectable + "', '" + vendor + "', '" +str(datetime.now())+ "') ON DUPLICATE KEY UPDATE last_seen='" + str(datetime.now()) + "';");
        conn.commit()
        conn.close()
    return devs

setup('/dev/ttyUSB0')
scanForDevices()

exit()
