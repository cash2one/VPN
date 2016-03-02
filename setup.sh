#!/bin/sh

wget https://raw.githubusercontent.com/zhengxujiang/Code/master/ubuntu_pptp.sh
sudo sh ubuntu_pptp.sh

wget https://raw.githubusercontent.com/zhengxujiang/Code/master/auto.py
python auto.py

cat > crontabfile << END
* 13 * * * python auto.py
END

crontab crontabfile
