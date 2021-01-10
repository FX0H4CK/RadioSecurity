#!/bin/sh

sudo apt install aircrack-ng
sudo apt install mariadb-client mariadb-server
echo port = 3306 >> /etc/mysql/my.cnf
sudo apt install libmariadb3 libmariadb-dev
sudo ./create_database.py
echo '# Run BLE Sniffer every minute' >> /etc/crontab
echo */5 * * * * root /home/kali/RadioSecurity/BLE/Sniffer/sniffer.py >> /etc/crontab
echo '# Run Wifi Sniffer ' >> /etc/crontab
echo '#@reboot root /home/kali/RadioSecurity/Wifi/Scripts/exec_airodump' >> /etc/crontab
echo '# Sort Wifi Data to MariaDB' >> /etc/crontab
echo * * * * * root /home/kali/RadioSecurity/Wifi/Scripts/Sort_Data.py >> /etc/crontab
echo '# Run Zigbee Sniffer' >> /etc/crontab
echo */6 * * * * root /home/kali/RadioSecurity/Zigbee/sniffer.sh >> /etc/crontab
echo '# run Webinterface' >> /etc/crontab
echo @reboot kali /home/kali/RadioSecurity/Web/Interface/web.py >> /etc/crontab


