
wget https://raw.githubusercontent.com/zhengxujiang/Code/master/centos_vpn.sh
chmod +x ./centos_vpn.sh
./centos_vpn.sh

sudo yum -y install epel-release
sudo yum -y install python-pip
sudo yum clean all
pip install requests

wget https://raw.githubusercontent.com/zhengxujiang/Code/master/auto2.py
python auto2.py

cat > crontabfile << END
00 13 * * * python auto2.py
END

crontab crontabfile
