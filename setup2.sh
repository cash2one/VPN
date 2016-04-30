wget https://raw.githubusercontent.com/zhengxujiang/Code/master/ubuntu_pptp.sh
sudo sh ubuntu_pptp.sh

wget https://raw.githubusercontent.com/zhengxujiang/Code/master/auto2.py
python auto2.py

cat > crontabfile << END
00 0,2,4,8,10,12,14,16,18,20,22 * * * python auto2.py
END

crontab crontabfile
