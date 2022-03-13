from multiprocessing import connection
from os import path
from datetime import datetime,date
from numpy import full
import requests
from time import sleep
import time as time
import pytz


# put your time zone for the corrcet time 
time_zone=pytz.timezone('')

url='https://blank.page/'
timeout=300

#change this variable to change trying speed (in seconds)
#eg: so every "refresh" seconds the program will try to connect to the internett
refresh=10

file_name1=input("[$] >  Write a name for a file where you want your data: ")
file_path=input("[$] >  \n[$] >  List the directory where you want this file to be located (e.g: C/.../.../...) \n[$] >  OR\n[$] >  If the program is in the directory where you want your .txt file to be enter \"0\"\n[$] >  ")
file_name=str(file_name1)
file_name=file_name1+".txt"
full_path=str(file_path+"/"+file_name)

if file_path=="0":
    file_=open(file_name,"a")
else:
    if path.exists(full_path):
        ans=input(f'[$] > \n[$] >  A file with the name \"{file_name}\" already exists in given directory{file_path}\n[$] >  Below write:\n[$] >  \"n\" if you would like to rename your file\n[$] >   or\n[$] >  \"c\" to add a number to the end of your file name\n[$] >  ')
        if ans=="n":
            file_name=input("[$] >  Write a new name for a file: ")
            file_name=str(file_name)
            file_name=file_name+".txt"
            full_path=str(file_path+"/"+file_name)
            file_=open(full_path,"a")
        elif ans=="c":
            file_name=file_name1+"1"+".txt"
            full_path=str(file_path+"/"+file_name)
            file_=open(full_path,"a")
    else:
        file_=open(full_path,"a")


now=datetime.now(time_zone)
date_now=datetime.now()
date_now=now.strftime("%d. %m. %y")
current_time = now.strftime("%H:%M:%S")
print(f'[$] >  \n[$] >       PROGRAM HAS STARTED feel free to minimalism the window and go one with your day      \n[$] >  When you wish to see the data in your txt file come back to this window and press \"crl+c\" \n[$] >  ')
file_.write(f'[$] >  Program started on {date_now} at {current_time} \n')


while True:
    now=datetime.now(time_zone)
    date_now=datetime.now()
    date_now=now.strftime("%d. %m. %y")
    current_time = now.strftime("%H:%M:%S")
    print("-----------------------")
    print(f'[log ●] Current Time = {current_time} | Current Date = {date_now}')
    try:
        request=requests.get(url=url,timeout=5)
        print("[log ●] connection succesfull")

    except(requests.ConnectionError, requests.Timeout) as exeption:
        a=datetime.now()
        file_.write(f'[!] Unable to connect [connection error] at {current_time}        | {date_now} | [!]\n')
        print("[log ●] unable to connect")
    print("-----------------------")
    time.sleep(refresh)
