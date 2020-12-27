#!/usr/bin/python3

import os
import mariadb
import subprocess
import json

from datetime import datetime

out = subprocess.check_output(['tshark', '-r', 'out.pcap', '-T', 'json'])
data = json.loads(out)


time_sniffed = datetime.now()

note = f"insert into zigbee(timestamp_sniffed) VALUES ('{time_sniffed}');"
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
    cursor.execute(note)
except mariadb.Error as e:
    print(f"Error {e}")
conn.commit()
conn.close()


for i in range(0,len(data)):
    try:
        index = data[i]['_index']
    except KeyError:
        continue
    try:
        ptype = data[i]['_type']
    except KeyError:
        continue
    try:
        score = data[i]['_score']
    except KeyError:
        continue
    try:
        frame_encap_type = data[i]['_source']['layers']['frame']['frame.encap_type']
    except KeyError:
        continue
    try:
        frame_time = data[i]['_source']['layers']['frame']['frame.time'].replace('  ',' 0')
    except KeyError:
        continue
    try:
        frame_time = frame_time[:-7]
    except KeyError:
        continue
    try:
        frame_time = datetime.strptime(frame_time,'%b %d, %Y %H:%M:%S.%f')
    except KeyError:
        continue
    try:
        frame_offset_shift = data[i]['_source']['layers']['frame']['frame.offset_shift']
    except KeyError:
        continue
    try:
        frame_time_epoch = data[i]['_source']['layers']['frame']['frame.time_epoch']
    except KeyError:
        continue
    try:
        frame_time_delta_displayed = data[i]['_source']['layers']['frame']['frame.time_delta_displayed']
    except KeyError:
        continue
    try:
        frame_time_delta = data[i]['_source']['layers']['frame']['frame.time_delta']
    except KeyError:
        continue
    try:
        frame_time_relative = data[i]['_source']['layers']['frame']['frame.time_relative']
    except KeyError:
        continue
    try:
        frame_number = data[i]['_source']['layers']['frame']['frame.number']
    except KeyError:
        continue
    try:
        frame_len = data[i]['_source']['layers']['frame']['frame.len']
    except KeyError:
        continue
    try:
        frame_cap_len = data[i]['_source']['layers']['frame']['frame.cap_len']
    except KeyError:
        continue
    try:
        frame_marked = data[i]['_source']['layers']['frame']['frame.marked']
    except KeyError:
        continue
    try:
        frame_ignored = data[i]['_source']['layers']['frame']['frame.ignored']
    except KeyError:
        continue
    try:
        frame_protocols = data[i]['_source']['layers']['frame']['frame.protocols']
    except KeyError:
        continue

    try:
        wpan_security = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.security']
    except KeyError:
        continue
    try:
        wpan_frame_type = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.frame_type']
    except KeyError:
        continue
    try:
        wpan_pending = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.pending']
    except KeyError:
        continue
    try:
        wpan_ack_request = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.ack_request']
    except KeyError:
        continue
    try:
        wpan_pan_id_compression = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.pan_id_compression']
    except KeyError:
        continue
    try:
        wpan_fcf_reserved = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.fcf.reserved']
    except KeyError:
        continue
    try:
        wpan_seqno_suppression = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.seqno_suppression']
    except KeyError:
        continue
    try:
        wpan_ie_present = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.ie_present']
    except KeyError:
        continue
    try:
        wpan_dst_addr_mode = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.dst_addr_mode']
    except KeyError:
        continue
    try:
        wpan_version = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.version']
    except KeyError:
        continue
    try:
        wpan_src_addr_mode = data[i]['_source']['layers']['wpan']['wpan.fcf_tree']['wpan.src_addr_mode']
    except KeyError:
        continue

   
    query=f"INSERT INTO zigbee(zigbee_index, zigbee_type, score, frame_encap_type, frame_time, frame_offset_shift, frame_time_epoch, frame_time_delta, frame_time_delta_displayed, frame_time_relative, frame_number, frame_len, frame_cap_len, frame_marked, frame_ingnored, frame_protocols, wpan_security, wpan_frame_type, wpan_pending, wpan_ack_request, wpan_pan_id_compression, wpan_fcf_reserved, wpan_seqno_suppression, wpan_ie_present, wpan_dst_addr_mode, wpan_version, wpan_src_addr_mode, timestamp_sniffed) VALUES ('{index}', '{ptype}', '{score}', {frame_encap_type},'{frame_time}', {frame_offset_shift}, {frame_time_epoch}, {frame_time_delta}, {frame_time_delta_displayed}, {frame_time_relative}, {frame_number}, {frame_len}, {frame_cap_len}, {frame_marked}, {frame_ignored}, '{frame_protocols}', {wpan_security}, {wpan_frame_type}, {wpan_pending}, {wpan_ack_request}, {wpan_pan_id_compression}, {wpan_fcf_reserved}, {wpan_seqno_suppression}, {wpan_ie_present}, '{wpan_dst_addr_mode}', {wpan_version}, '{wpan_src_addr_mode}', '{time_sniffed}');"
    print(query)


   # wpan_seq_no = data[i]['_source']['layers']['wpan']['wpan.seq_no']
   # ws_expert_message = data[i]['_source']['layers']['wpan']['_ws.expert']['_ws.expert.message']
   # ws_expert_severity = data[i]['_source']['layers']['wpan']['_ws.expert']['_ws.expert.severity']
   # ws_expertgroup = data[i]['_source']['layers']['wpan']['_ws.expert']['_ws.expert.group']
   # ws_malformed = data[i]['_source']['layers']['wpan']['_ws.malformed']

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
        cursor.execute(query)
    except mariadb.Error as e:
        print(f"Error {e}")
    conn.commit()
    conn.close()
