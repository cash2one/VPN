#! /bin/bash

sudo apt-get install pptpd
read inputA<<Y

sed -i '$a localip 10.10.0.1' /etc/pptpd.conf
sed -i '$a remoteip 10.10.0.2-255' /etc/pptpd.conf

sed -i '$a ms-dns 8.8.8.8' /etc/ppp/pptpd-options

sed -i '$a zxj * zxj1234 *' /etc/ppp/chap-secrets

sed -i '$a net.ipv4.ip_forward=1' /etc/sysctl.conf
sudo sysctl -p
