#!/usr/bin/python3

import csv
import os
import mariadb
import sys
import requests
import time

while True:
    with open ('../Raw/scan-01.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader,None) #Skip first Line
        next(reader,None)
        for row in reader:
            if len(row)==15:
                r = requests.get('https://api.macvendors.com/'+row[0]);
                vendor = r.text
                time.sleep(1)
                try:
                    conn = mariadb.connect(
                            user="writer",
                            password="PW4Writer!",
                            host="127.0.0.1",
                            port=3306,
                            database="radio_mon"

                    )
                except mariadb.Error as e:
                    print(f"Error connecting to MariaDB: {e}")

                cursor = conn.cursor()
                try:
                    cursor.execute("INSERT INTO ssids(bssid,first_seen,last_seen,channel,speed,privacy,cipher,auth,power,beacons,iv,ip,length,essid, vendor) VALUES ('" + row[0] +"', '" + row[1] +"', '" + row[2] +"', " + row[3] +", " + row[4] +", '" + row[5] +"', '" + row[6] +"', '" + row[7] +"', " + row[8] +", " + row[9] +", " + row[10] +", '" + row[11] +"', " + row[12] +", '" + row[13] + "', '"+ vendor + "') ON DUPLICATE KEY UPDATE last_seen='" + row[2] + "';")
                except mariadb.Error as e:
                    print(f"Error: {e}")
                conn.commit()


            elif len(row)==7:
                with open('../Raw/Clients.csv', 'a', newline='') as clients:
                    wrclients = csv.writer(clients)
                    wrclients.writerow(row)
    time.sleep(60)
