#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import re
import sys,os
import socket
from random import Random

class WeiXin:
	def __init__(self):
		# 公众号登陆账号密码
		self.unm = "gdst.zxj@gmail.com"
		self.pwd = "1d49ab88e526672ea1adb5de79d4f8ca"
		self.token = ''
		self.fakeid = ''
		# 字典存储用户与fakeid的关系
		self.users = {}
		# session自动处理cookies
		self.session = requests.Session()

	def login(self):
		# 登陆
		headers = {
		"Host": "mp.weixin.qq.com",
		"Referer": "https://mp.weixin.qq.com/",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
		}
		data = {
		"username": self.unm,
		"pwd": self.pwd,
		"imgcode": '',
		"f": "json"
		}
		url_login = "https://mp.weixin.qq.com/cgi-bin/login"
		r_login = self.session.post(url_login,data=data,headers=headers)
		try:
			self.token = re.findall("token=(\d*)",r_login.content)[0]
			print ("token ",self.token)
			if self.token != '':
				print ("login success and get token!")
				# 登陆之后转入首页，可去掉
				url_index = "https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=%s" % self.token
				r_index = self.session.get(url_index)
				if r_index.status_code == 200:
					print ("get the index")
				else:
					print ("get index failed")
			else:
				print ("login failed")
		except:
			print ("get token error")
		

	def change_pass(self,my_ip,password,msg_id):
		#修改密码
		f = open('/etc/ppp/chap-secrets', 'r+')
		flist = f.readlines()
		flist[2] = 'jdvpn pptpd %s * \n ' % password
		f = open('/etc/ppp/chap-secrets', 'w+')
		f.writelines(flist)
		url_fodder = "https://mp.weixin.qq.com/cgi-bin/operate_appmsg?t=ajax-response&sub=update&type=10&token=%s&lang=zh_CN" % self.token
		fod_headers = {
		"Host" : "mp.weixin.qq.com",
		"Origin" : "https://mp.weixin.qq.com",
		"Referer" : "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&lang=zh_CN&token=%s&type=10&appmsgid=%s&isMul=1" % (self.token,msg_id) ,
		"User-Agent:" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"
		}
		fod_data = {
		"token" : self.token ,
		"lang" : "zh_CN",
		"f" : "json",
		"ajax" : "1",
		"random" : "0.05823731515556574",
		"AppMsgId" : msg_id,
		"count" : "1",
		"title0" : "免费VPN账号（线路一）",
		"content0" : '<p style="text-align: center;"><span style="color: rgb(0, 0, 0);"><strong><span style="font-family: Tahoma, Arial, Helvetica, sans-serif; line-height: normal; font-size: 20px;">免费VPN，高速稳定，两个小时更一次换密码。</span></strong></span></p><p style="text-align: center;"><font face="Tahoma, Arial, Helvetica, sans-serif"><span style="font-size: 20px; line-height: normal;"><b>线路一：日本服务器</b></span></font></p><p style="text-align: center;"><span style="color: rgb(0, 0, 0);"><strong><span style="color: rgb(0, 0, 0); line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;">服务器：freejp.jdvpn.online</span></strong></span><span style="color: rgb(0, 0, 0);"><strong><span style="font-family: Tahoma, Arial, Helvetica, sans-serif; line-height: normal; font-size: 20px;"></span></strong></span></p><p style="text-align: center;"><span style="color: rgb(0, 0, 0);"><strong><span style="line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;">账号：jdvpn</span></strong></span></p><p style="text-align: center;"><span style="color: rgb(0, 0, 0);"><strong><span style="line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;">密码：%s</span></strong><strong><span style="line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;"></span></strong><strong><span style="line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;"></span></strong></span></p><p style="text-align: center;"><span style="color: rgb(0, 0, 0);"><strong><span style="line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;">协议：pptp</span></strong><strong><span style="line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;"></span></strong><strong><span style="line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;"></span></strong><strong><span style="line-height: normal; font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 20px;"></span></strong></span></p><p style="text-align: center;"><font face="Tahoma, Arial, Helvetica, sans-serif"><span style="font-size: 20px; line-height: normal;"><b>请根据自身网络选择适当的免费服务器</b></span></font></p><p><span style="color: rgb(51, 51, 51); font-family: Tahoma, Arial, Helvetica, sans-serif; font-size: 15px; line-height: normal; background-color: rgb(244, 244, 244);"></span><br/></p>' % (password),
		"digest0" : "免费VPN，高速稳定，两个小时更一次换密码。",
		"author0" : '',
		"fileid0" : "401191126",
		"music_id0" : '',
		"video_id0" : '',
		"show_cover_pic0" : "0",
		"shortvideofileid0" : '',
		"copyright_type0" : "0",
		"can_reward0" : "0",
		"reward_wording0" : '',
		"need_open_comment0" : '0',
		"sourceurl0" : '',
		"free_content0" : '',
		"fee0" : "0"
		} 

		r_fod = self.session.post(url_fodder, data=fod_data, headers=fod_headers);
		err_msg = re.findall("\"err_msg\":\"(.*?)\"",r_fod.content)[0]
		if  err_msg == 'ok':
			print "Password is %s" % password
			f = open('/etc/ppp/chap-secrets', 'r+')
			flist = f.readlines()
			flist[3] = 'jdvpn pptpd %s * \n' % password
			f = open('/etc/ppp/chap-secrets', 'w+')
			f.writelines(flist)

		else :
			self.change_pass(my_ip,password,msg_id)
			print "Fail to change the password"

		

	def run(self,my_ip,password,msg_id):
		self.login()
		self.change_pass(my_ip,password,msg_id)
		

def random_str(randomlength):
    str = ''
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def get_my_ip():
	#获取本机IP
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "系统维护中"

wx = WeiXin()
password = random_str(6)
my_ip = get_my_ip()
wx.run(my_ip,password,'401187489')
wx.run(my_ip,password,'401187489')


