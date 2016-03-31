
wget https://raw.githubusercontent.com/zhengxujiang/Code/master/centos_vpn.sh
chmod +x ./centos_vpn.sh
./centos_vpn.sh

wget https://raw.githubusercontent.com/zhengxujiang/Code/master/auto2.py
python auto2.py

cat > crontabfile << END
00 13 * * * python auto2.py
END

crontab crontabfile
