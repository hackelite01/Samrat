#!/usr/local/bin/python
# coding: latin-1
#if you use this code give me credit @hackelite01
#i do not give you permission to show / edit this script without my credit
#to ask questions or report a problem message me on instagram @hackelite01
"""

 

"""
import os
import sys
import random
lred = '\033[91m'
lblue = '\033[94m'
lgreen = '\033[92m'
yellow = '\033[93m'
cyan = '\033[1;36m'
purple = '\033[95m'
red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
orange = '\033[33m'

colorlist = [red, blue, green, yellow, lblue, purple, cyan, lred, lgreen, orange]
randomcolor = random.choice(colorlist)
banner3list = [red, blue, green, purple]

def anonoff():
	print ("\033[93m------------------------\033[0m")
	print ("\nSTOPPING MACCHANGER\n")
	print ("\033[93m------------------------\033[0m")
	os.system("iwconfig")
	k = raw_input("Interface: ")
	c = 'ifconfig {0} down'.format(k)
	os.system(c)
	os.system("macchanger -p " + k)
	s = 'ifconfig {0} up'.format(k)
	os.system(s)
	sys.exit()
	reboot()
anonoff()
