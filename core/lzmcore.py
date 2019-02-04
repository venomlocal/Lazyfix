## lzmfix.py - useful module of Lazyfix
# -*- coding: utf-8 -*-
import os
import sys
import time

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'

lazyfix_banner = """
▒█░░░ ░█▀▀█ ▒█▀▀▀█ ▒█░░▒█ ▒█▀▀▀ ▀█▀ ▀▄▒▄▀ 
▒█░░░ ▒█▄▄█ ░▄▄▄▀▀ ▒█▄▄▄█ ▒█▀▀▀ ▒█░ ░▒█░░ 
▒█▄▄█ ▒█░▒█ ▒█▄▄▄█ ░░▒█░░ ▒█░░░ ▄█▄ ▄▀▒▀▄      
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Lazyfix
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("lzfix > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		restart_program()

def banner():
	print lazyfix_banner

def vpn():
	print '\n###### Installing VPN(for kali)'
	os.system('apt update && apt upgrade')
	os.system('apt-get install network-manager-openvpn-gnome')
	os.system('apt-get install network-manager-pptp')
	os.system('apt-get install network-manager-pptp-gnome')
        os.system('apt-get install network-manager-strongswan')
        os.system('apt-get install network-manager-vpnc')
        os.system('apt-get install network-manager-vpnc-gnome')
        os.system('/etc/init.d/network-manager restart')
	print '###### Done'
	print "###### 'your vpn ready' to start."
	backtomenu_option()

def tor():
	print '\n###### Installing TOR'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('apt-get install tor')
	print '###### Done'
        print "###### type 'tor' to start."
	backtomenu_option()

def gpg_error():
	print '\n###### Installing gpg_error'
	os.system('apt update && apt upgrade')
	os.system('apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6')
        os.system('apt-get update')
	print '###### Done'
        print "###### your problem solved."
	backtomenu_option()

def sources_kali1():
	print '\n######  sources.list for kali 1.0'
	print 'deb http://old.kali.org/kali moto main non-free contrib'
        print '# For source package access, uncomment the following line'
	print '# deb-src http://old.kali.org/kali moto main non-free contrib'
        print "###### copie this sources in /etc/apt/sources.list."
	backtomenu_option()

def sources_kali2():
	print '\n######  sources.list for kali 2.0'
	print 'deb http://http.kali.org/kali kali-rolling main non-free contrib'
        print 'deb-src http://http.kali.org/kali kali-rolling main non-free contrib'
        print "###### copie this sources in /etc/apt/sources.list."
	backtomenu_option()

def MY_IP():
	print bcolors.OKGREEN + "\n   your ip is in lign eth0 or wlan0\n" + bcolors.ENDC
        os.system('ifconfig')
        print bcolors.OKGREEN + "\n   your ip is in lign eth0 or wlan0\n" + bcolors.ENDC
	backtomenu_option()


