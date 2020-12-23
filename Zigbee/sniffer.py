#!/usr/bin/python3

import os
import mariadb
import subprocess
import json

out = subprocess.check_output(['tshark', '-r', 'out.pcap', '-T', 'jsonraw'])
data = json.loads(out)
print(data[1]['_score'])
print(len(data))
print(type(data))
