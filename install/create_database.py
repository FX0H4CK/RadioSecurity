#!/usr/bin/python3

import os
import mariadb

try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")

cursor = conn.cursor()
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS radio_mon;")
    conn.close()

except mariadb.Error as e:
    print(f"Error creating DB: {e}")

print("[i] Database created")

