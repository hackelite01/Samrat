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

def mainbanner1():
	print ("""
\033[0m
 
,d88~~\                                            d8   \033[35m
8888      /~~~8e  888-~88e-~88e 888-~\   /~~~8e  _d88__ \033[0m
`Y88b         88b 888  888  888 888          88b  888   \033[35m
 `Y88b,  e88~-888 888  888  888 888     e88~-888  888   \033[0m
   8888 C888  888 888  888  888 888    C888  888  888   \033[35m
\__88P'  "88_-888 888  888  888 888     "88_-888  "88_/ 
	\n""".decode('utf-8'))

def mainbanner2():
	print ("""\033[34m
  ________     __       ___      ___   _______        __  ___________  \033[94m
 /"       )   /""\     |"  \    /"  | /"      \      /""\("     _   ") \033[1;36m
(:   \___/   /    \     \   \  //   ||:        |    /    \)__/  \\__/  \033[94m
 \___  \    /' /\  \    /\\  \/.    ||_____/   )   /' /\  \  \\_ /     \033[1;36m
  __/  \\  //  __'  \  |: \.        | //      /   //  __'  \ |.  |     \033[94m
 /" \   :)/   /  \\  \ |.  \    /:  ||:  __   \  /   /  \\  \\:  |     \033[1;36m
(_______/(___/    \___)|___|\__/|___||__|  \___)(___/    \___)\__|     
                                                                      
	\033[0m
	\n""".decode('utf-8'))

def mainbanner3():
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
	""".decode('utf-8').format(random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list)))

def mainbanner4():
	print ("""\033[93m
     _______.     ___      .___  ___. .______          ___   .___________.\033[91m
    /       |    /   \     |   \/   | |   _  \        /   \  |           |\033[33m
   |   (----`   /  ^  \    |  \  /  | |  |_)  |      /  ^  \ `---|  |----`\033[93m
    \   \      /  /_\  \   |  |\/|  | |      /      /  /_\  \    |  |     \033[91m
.----)   |    /  _____  \  |  |  |  | |  |\  \----./  _____  \   |  |     \033[33m
|_______/    /__/     \__\ |__|  |__| | _| `._____/__/     \__\  |__| \033[0m
	\033[0m
	\033[0m\n""".decode('utf-8'))

def mainbanner5():
	print ("""\033[92m
                                                                            
           .                                                                   
          ;W                                 j.                                
         f#E         ..           ..       : EW,                   .. GEEEEEEEL\033[92m
       .E#f         ;W,          ,W,     .Et E##j                 ;W, ,;;L#K;;.\033[0m
      iWW;         j##,         t##,    ,W#t E###D.              j##,    t#E   \033[92m
     L##Lffi      G###,        L###,   j###t E#jG#W;            G###,    t#E   \033[0m
    tLLG##L     :E####,      .E#j##,  G#fE#t E#t t##f         :E####,    t#E   \033[92m
      ,W#i     ;W#DG##,     ;WW; ##,:K#i E#t E#t  :K#E:      ;W#DG##,    t#E   \033[0m
     j#E.     j###DW##,    j#E.  ##f#W,  E#t E#KDDDD###i    j###DW##,    t#E   \033[92m
   .D#j      G##i,,G##,  .D#L    ###K:   E#t E#f,t#Wi,,,   G##i,,G##,    t#E   \033[0m
  ,WK,     :K#K:   L##, :K#t     ##D.    E#t E#t  ;#W:   :K#K:   L##,    t#E   \033[92m
  EG.     ;##D.    L##, ...      #G      ..  DWi   ,KK: ;##D.    L##,     fE   \033[0m
  ,       ,,,      .,,           j                      ,,,      .,,       :   \033[92m
       
	""".decode('utf-8'))

def mainbanner6():
	print ("""
 \033[0m
 ________     __       ___      ___   _______        __  ___________  \033[91m
 /"       )   /""\     |"  \    /"  | /"      \      /""\("     _   ") \033[33m
(:   \___/   /    \     \   \  //   ||:        |    /    \)__/  \\__/  \033[93m
 \___  \    /' /\  \    /\\  \/.    ||_____/   )   /' /\  \  \\_ /     \033[92m
  __/  \\  //  __'  \  |: \.        | //      /   //  __'  \ |.  |     \033[94m
 /" \   :)/   /  \\  \ |.  \    /:  ||:  __   \  /   /  \\  \\:  |     \033[1;36m
(_______/(___/    \___)|___|\__/|___||__|  \___)(___/    \___)\__|     \033[95m
                 
	""".decode('utf-8'))
def mainbanner7():
	print ("""\033[92m
                                               .         .                                                              
   d888888o.           .8.                   ,8.       ,8.          8 888888888o.            .8.    8888888 8888888888 \033[0m
 .`8888:' `88.        .888.                 ,888.     ,888.         8 8888    `88.          .888.         8 8888       \033[92m
 8.`8888.   Y8       :88888.               .`8888.   .`8888.        8 8888     `88         :88888.        8 8888       \033[0m
 `8.`8888.          . `88888.             ,8.`8888. ,8.`8888.       8 8888     ,88        . `88888.       8 8888       \033[92m
  `8.`8888.        .8. `88888.           ,8'8.`8888,8^8.`8888.      8 8888.   ,88'       .8. `88888.      8 8888       \033[0m
   `8.`8888.      .8`8. `88888.         ,8' `8.`8888' `8.`8888.     8 888888888P'       .8`8. `88888.     8 8888       \033[92m
    `8.`8888.    .8' `8. `88888.       ,8'   `8.`88'   `8.`8888.    8 8888`8b          .8' `8. `88888.    8 8888       \033[0m
8b   `8.`8888.  .8'   `8. `88888.     ,8'     `8.`'     `8.`8888.   8 8888 `8b.       .8'   `8. `88888.   8 8888       \033[92m
`8b.  ;8.`8888 .888888888. `88888.   ,8'       `8        `8.`8888.  8 8888   `8b.    .888888888. `88888.  8 8888       \033[0m
 `Y8888P ,88P'.8'       `8. `88888. ,8'         `         `8.`8888. 8 8888     `88. .8'       `8. `88888. 8 8888       

	""".decode('utf-8'))

def mainbanner8():
	print ("""\033[0m
 
,d88~~\                                            d8   \033[35m
8888      /~~~8e  888-~88e-~88e 888-~\   /~~~8e  _d88__ \033[0m
`Y88b         88b 888  888  888 888          88b  888   \033[35m
 `Y88b,  e88~-888 888  888  888 888     e88~-888  888   \033[0m
   8888 C888  888 888  888  888 888    C888  888  888   \033[35m
\__88P'  "88_-888 888  888  888 888     "88_-888  "88_/ 
       
	\033[0m""".decode('utf-8'))

def mainbanner9():
	print ("""\033[31m
    _______.     ___      .___  ___. .______          ___   .___________.\033[91m
    /       |    /   \     |   \/   | |   _  \        /   \  |           |\033[33m
   |   (----`   /  ^  \    |  \  /  | |  |_)  |      /  ^  \ `---|  |----`\033[93m
    \   \      /  /_\  \   |  |\/|  | |      /      /  /_\  \    |  |     \033[91m
.----)   |    /  _____  \  |  |  |  | |  |\  \----./  _____  \   |  |     \033[33m
|_______/    /__/     \__\ |__|  |__| | _| `._____/__/     \__\  |__| 
	\033[0m""".decode('utf-8'))

def mainbanner():
	import random
	for x in range(10):
	  num = random.randint(1,9)
	if num == 1:
		mainbanner1()
	if num == 2:
		mainbanner2()
	if num == 3:
		mainbanner3()
	if num == 4:
		mainbanner4()
	if num == 5:
		mainbanner5()
	if num == 6:
		mainbanner6()
	if num == 7:
		mainbanner7()
	if num == 8:
		mainbanner8()
	if num == 9:
		mainbanner9()

mainbanner()
