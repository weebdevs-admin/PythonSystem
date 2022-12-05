from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import configparser
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
#import pyttsx3
import requests
time.sleep(0.9)


re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
os.system("pip install pyttsx3")
os.system("clear")
print(f"""{cy}downloading:""")


time.sleep(1)
print(f"""
    {re}  _ _           ____        _
    {re}  |  \/  |_   _ _| (_)_  _ |  )  _ | |_
    {re}  | |\/| | | | / | | | '_  _ \|  _ \ / _ \| __|
    {re}  | |  | | |_| \__ \ | | | | | | | |_) | (_) | |_
    {re}  |_|  |_|\__,_|___/_|_|_| |_| |_|____/ \___/ \__|
                                                                                                                                                                                                                                            
           
                                                                                                                                                                                                                                                   Version : 1.01
	{re}DASTURIMIZGA XUSH KELIBSIZ
	{cy}https://t.me/TaqvimMuslimBot
	""")

print (f""" _________Tayyormisiz__________ \n {cy}>>>>>>>{re}_MuslimBot_{cy}<<<<<<<<<<< """) 

ism = input(f"""{re}ismingizni kiriting: \n >>>""" )
print(f"""{cy}Assalomu alikum dasturimizga xush kelibsan  """  + ism.title())



#pyttsx3.speak("всем привет " + ism )


harf = input(f"""{re}Istalgan tugmani bosing \n >>>""")


print(f"""{cy}>>> 1.Botga tashrif buyurish.""")
print(f"""{cy }>>>2.telegram members""")
print(f"""{cy}>>> 3.my games""")
print(f"""{cy}>>> 4.hackers tools""") 
print(f"""{cy}>>> 5.siz haqingizdagi malumot""")

#pyttsx3.speak("привет добро пожаловать в нашу программу.рад,что вы выбрали нас. перейдите к следуюшему шагу")


a = input(f"""{cy} >>>""")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')


if a == "1":
     webbrowser.open('https://t.me/TaqvimmuslimBot')
     time.sleep(3)
     print(f"""{re} botimizdan foydalanganingiz uchun rahmat ^_^\n >>>>""" + ism.title())
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
    print(f"""{cy}sizning ismingiz\n >>>   """ + ism.title())
    print("siz bizning aktiv foydalanuvchilarimiz qatoridasiz""")
    print(f"""Dasturimiz sizga yoqqan bolsa biz hursand bo'lamiz """ + ism)
    sozlama = input(f"""{re}1.ismi ozgartirish \n >>> """)
  
    if sozlama == "1":
        print("yangi ism kiriting ")
        d = input(">>>")
        print(f"""ism o'zgartirildi sizning ismingiz """ +d.title())
    else:
        print(f"""{re}EROR""")

else:
    print(f"""EROR""")










