#!/bin/sh

wget https://raw.githubusercontent.com/zhengxujiang/Code/master/ubuntu_pptp.sh
sudo sh ubuntu_pptp.sh

wget https://raw.githubusercontent.com/zhengxujiang/Code/master/auto.py
python auto.py

cat > crontabfile << END
00 0,2,4,6,8,10,12,14,16,18,20,22 * * * python auto.py
END

crontab crontabfile
