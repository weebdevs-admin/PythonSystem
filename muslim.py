import os
import sys
import csv
import traceback
import time
import random
import time
import os 
import webbrowser 
import json
import random
install configparser
time.sleep(0.9)
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
os.system("pip install requests")
os.system("pip install configparser")
os.system("pip install python3")
os.system("clear")
print(f"""{cy}installing [+]""")

time.sleep(1)
print(f"""
    {re}  _ _           ____        _
    {re}  |  \/  |_   _ _| (_)_  _ |  )  _ | |_
    {re}  | |\/| | | | / | | | '_  _ \|  _ \ / _ \| __|
    {re}  | |  | | |_| \__ \ | | | | | | | |_) | (_) | |_
    {re}  |_|  |_|\__,_|___/_|_|_| |_| |_|____/ \___/ \__|
                                                                                                                                                                                                                                            
 """)

print (f""" {cy}>>>>>>>{re}version 1.1.3{cy}<<<<<<<<<<< """) 

ism = input(f"""{re}username: \n >>>""" )
print(f"""{cy}Welcome to  """  + ism.title())
harf = input(f"""{re}.... """)
print(f"""{cy}>>> 1.Open telegram bot """)
print(f"""{cy }>>>2.Telegram members""")
print(f"""{cy}>>> 3.My games""")
print(f"""{cy}>>> 4.Hackers tools""") 
print(f"""{cy}>>> 5.My abaut""")
a = input(f"""{cy} >>>""")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')


if a == "1":
     webbrowser.open('https://t.me/TaqvimmuslimBot')
     time.sleep(3)
     print(f"""{re} Open width browser ^_^\n >>>>""" + ism.title())
elif a == "2":
    print(gr+"[+] Installing requierments ...")
    os.system('python3 -m pip install telethon')
    os.system('pip3 install telethon')
    os.system("touch config.data")
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    os.system("clear")
    print(f""" 	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
{re}╚═╗{cy}├┤  │ │ │├─┘
{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")
    xid = input(gr+"[+] enter api ID : "+re)
    cpass.set('cred', 'id', xid)
    xhash = input(gr+"[+] enter hash ID : "+re)
    cpass.set('cred', 'hash', xhash)
    xphone = input(gr+"[+] enter phone number : "+re)
    cpass.set('cred', 'phone', xphone)
    setup = open('config.data', 'w')
    cpass.write(setup)
    setup.close()
    print(gr+"[+] setup complete !")
    print(gr+"[+] now you can run any tool !")
    print(gr+"[+] make sure to read docs 4                        installation & api setup")
   
elif a == "5":
    os.system("clear")
    print(f"""{re}>>>MYNAME<<< """)
    print(f"""{cy}User Name\n >>>   """ + ism.title())
    print("Undefined")
    sozlama = input(f"""{re}1.User settings \n >>> """)
  
    if sozlama == "1":
        print("New User Name")
        d = input(">>>")
        print(f"""New Name""" +d.title())
    else:
        print(f"""{re}EROR""")

else:
    print(f"""EROR""")










