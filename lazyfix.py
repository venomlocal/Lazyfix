## lazyfix.py - Lazyfix v1.0
# -*- coding: utf-8 -*-
##
import os
import sys
from time import sleep as timeout
from core.lzmcore import *

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'


def main():
	banner()
	print " [01] FIX KALI ERROR" 
        print " [02] SOURCES.LIST"
        print " [03] MY_IP"
	print bcolors.BOLD + "\n   [10] Exit the fixkali\n" + bcolors.ENDC
	lazyfix = raw_input("fix > ")
  
	if lazyfix == "1" or lazyfix == "01":
		print bcolors.OKGREEN + "    [01] vpn" + bcolors.ENDC
		print bcolors.OKGREEN + "    [02] tor"  + bcolors.ENDC
                print bcolors.OKGREEN + "    [03] gpg_error" + bcolors.ENDC
	        print bcolors.BOLD + "\n    [00] Back to main menu \n" + bcolors.ENDC
		fixkali = raw_input("fix > ")
		
		if fixkali == "01" or fixkali == "1":
			vpn()
		elif fixkali == "02" or fixkali == "2":
			tor()
                elif fixkali == "03" or fixkali == "3":
			gpg_error()  
		elif fixkali == "00" or fixkali == "0":
			restart_program()
		else:
			print bcolors.FAIL + "\nERROR: Wrong Input" + bcolors.ENDC
			timeout(2)
			restart_program()


        elif lazyfix == "2" or lazyfix == "02":
		print bcolors.OKGREEN + "\n    [01] sources_kali1" + bcolors.ENDC
		print bcolors.OKGREEN + "    [02] sources_kali2" + bcolors.ENDC
	        print bcolors.BOLD + "\n    [00] Back to main menu\n" + bcolors.ENDC
		sources = raw_input("fix > ")
		
		if sources == "01" or sources == "1":
			sources_kali1()
		elif sources == "02" or sources == "2":
			sources_kali2()
		elif sources == "00" or sources == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()

        elif lazyfix == "3" or lazyfix == "03":
                 MY_IP()

	elif lazyfix == "10":
		sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()