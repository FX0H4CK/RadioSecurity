#!/bin/sh

sudo apt install aircrack-ng
cd /usr/local/src
wget  -O re4son-kernel_current.tar.xz https://re4son-kernel.com/download/re4son-kernel-current/
tar -xJf re4son-kernel_courrent.tar.xz
cd re4son-kernel_4*
sudo ./install.sh
sudo apt install mariadb-client mariadb-server
echo port = 3306 >> /etc/mysql/my.cnf
