#!/bin/sh

sudo apt install aircrack-ng
sudo apt install mariadb-client mariadb-server
echo port = 3306 >> /etc/mysql/my.cnf
