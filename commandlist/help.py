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
def helpbanner():
	a = os.popen("ls commandlist -1 | wc -l").read()
	b = a.replace('\n', '')
	print ("""
╔══════════════════════════════════════════════════════════╗
║                                                   ║ 
║  \033[92m  .S    S.     sSSs  S.       .S_sSSs   \033[0m ║
║  \033[90m .SS    SS.   d%%SP  SS.     .SS~YS%%b  \033[0m ║
║  \033[92m S%S    S%S  d%S'    S%S     S%S   `S%b \033[0m ║
║  \033[90m S%S    S%S  S%S     S%S     S%S    S%S \033[0m ║
║  \033[92m S%S SSSS%S  S&S     S&S     S%S    d*S \033[0m ║
║  \033[94m S&S  SSS&S  S&S_Ss  S&S     S&S   .S*S \033[0m ║
║  \033[90m S&S    S&S  S&S~SP  S&S     S&S_sdSSS  \033[0m ║
║  \033[94m S&S    S&S  S&S     S&S     S&S~YSSY   \033[0m ║
║  \033[90m S*S    S*S  S*b     S*b     S*S        \033[0m ║
║  \033[94m S*S    S*S  S*S.    S*S.    S*S        \033[0m ║
║  \033[90m S*S    S*S   SSSbs   SSSbs  S*S        \033[0m ║
║  \033[94m SSS    S*S    YSSP    YSSP  S*S        \033[0m ║
║  \033[90m        SP                   SP         \033[0m ║
║  \033[94m        Y                    Y          \033[0m ║            
║                                                  ║     
║══════════════════════════════════════════════════════════║
║             Commands: [\033[32m{0}\033[0m]    Banners: [\033[31m6\033[0m]                ║  
║══════════════════════════════════════════════════════════════════════════════════════╗
║ ?        | this menu                                                                 ║
║ exit     | exit Samrat                                                                 ║
║ clear    | clears screen                                                             ║
║ banner   | shows a banner                                                            ║
║ infoscan | gather information on a host [for a more specific scan type infoscan -o]  ║
║ dos      | run Denial-Of-Service attacks                                             ║
║                                                                                      ║
║                                                                                      ║
║                                      \033[5m@hackelite01\033[0m                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
	\033[0m\n""".format(b))
helpbanner()
