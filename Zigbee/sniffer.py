#!/usr/bin/python3

import os
import mariadb
import subprocess
import json

out = subprocess.check_output(['tshark', '-r', 'out.pcap', '-T', 'json'])
data = json.loads(out)
print(json.dumps(data))
for i in range(0,9):
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
        cursor.execute("INSERT INTO zigbee VALUES ('" + json.dumps(data) + "');")
    except mariadb.Error as e:
        print(f"Error {e}")

    conn.commit()
    conn.close()
    
    wpan_security = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.security']

    print(wpan_security)
