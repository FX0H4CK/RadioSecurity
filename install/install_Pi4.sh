#!/bin/sh
echo [*] Updating
sudo apt update
echo [*] installing Aircrack
sudo apt install aircrack-ng
echo [*] installing MariaDB
sudo apt install mariadb-client mariadb-server
sudo pip install mariadb
sudo pip3 install mariadb
echo [*] configure MariaDB
echo port = 3306 >> /etc/mysql/my.cnf
sudo apt install libmariadb3 libmariadb-dev
echo [*] configure crontab
sudo echo '# Run BLE Sniffer every minute' >> /etc/crontab
sudo echo '*/5 * * * * root /home/kali/RadioSecurity/BLE/Sniffer/sniffer.py' >> /etc/crontab
sudo echo '# Run Wifi Sniffer ' >> /etc/crontab
sudo echo '#@reboot root /home/kali/RadioSecurity/Wifi/Scripts/exec_airodump' >> /etc/crontab
sudo echo '# Sort Wifi Data to MariaDB' >> /etc/crontab
sudo echo '* * * * * root /home/kali/RadioSecurity/Wifi/Scripts/Sort_Data.py' >> /etc/crontab
sudo echo '# Run Zigbee Sniffer' >> /etc/crontab
sudo echo '*/6 * * * * root /home/kali/RadioSecurity/Zigbee/sniffer.sh' >> /etc/crontab
sudo echo '# run Webinterface' >> /etc/crontab
sudo echo '@reboot kali /home/kali/RadioSecurity/Web/Interface/web.py' >> /etc/crontab
sudo echo '@reboot service mysql start' >> /etc/crontab
echo [*] starting MariaDB
sudo service mysql start
echo [*] Restore MariaDB
sudo mysql < ../Backup/dump.sql

