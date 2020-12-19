#!/usr/bin/python3

import csv
import os

os.remove('../Raw/SSIDs.csv')
os.remove('../Raw/Clients.csv')

with open ('../Raw/scan-01.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        if len(row)==15:
            with open('../Raw/SSIDs.csv', 'a', newline='') as ssids:
                wr = csv.writer(ssids, quoting=csv.QUOTE_ALL)
                wr.writerow(row)

        elif len(row)==7:
            with open('../Raw/Clients.csv', 'a', newline='') as clients:
                wrclients = csv.writer(clients)
                wrclients.writerow(row)
