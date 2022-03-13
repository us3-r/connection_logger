
from multiprocessing import connection
from os import path
import os
from datetime import datetime,date
import re
from timeit import repeat
from numpy import full
import requests
from time import sleep
import time
import pytz
import argparse

tzlist=[]
for time_ in pytz.all_timezones:
    tzlist.append(time_)

parser=argparse.ArgumentParser(description="commands")

parser.add_argument('-f', help="Name of your file",type=str,default="conn_log")

parser.add_argument('-d',help="Name of your files directory",type=str, default=os.getcwd())

parser.add_argument('-t',help="your timezone",type=str,default='Europe/Ljubljana')

parser.add_argument('-u',help="url to desired website",type=str,default='https://blank.page/')

parser.add_argument('-r',help="time after which program will try to reconnect to the site",type=int)

args=parser.parse_args()
################### EXERTIONS FOR ARG VALUES ###################
print("\n")
#set file name
file_name1=args.f

#set file directory
file_path=""
fp=args.d
if fp=="0":
    #get current working directori
    file_path=os.getcwd()
else:
    file_path=fp 

#set time zone
if args.t!=" ":
    timezon=args.t
    if timezon in tzlist:
        tz=timezon
    else:
        tz='Europe/Ljubljana'
        print(f'[!] Entered timezone \"{timezon}\" is not in supported timezones; timezone is set to {tz} [!]')
else:
    tz='Europe/Ljubljana'

#set url
url='https://blank.page/'
if args.u!=" ":
    try:
        url_=args.u
        request=requests.get(url_,timeout=10)
        url=args.u
    except requests.exceptions.RequestException as ex:
        print(f'[!] There was an error with given url \"{args.u}\" new url is \"{url}\" [!]')
        url=url

#set repeat
new_r=args.r
if new_r<10:
    print(f'[!] For safety reasons this number should be bigger than 10 > so I set it to 10 :) [!]\n')
    rep=10
else:
    rep=args.r
################################################################

tz=tz
rep=float(rep)
time_zone=pytz.timezone(tz)
timeout=300

###  create file name and file path  ###
file_name=str(file_name1)
file_name=file_name1+".txt"
full_path=str(file_path+"/"+file_name)

###  open .txt file  ###
file_=open(full_path,"a")

### print all values  ###
print(f'| File name: {file_name}\n| File directory: {full_path}\n| Timezone: {tz}\n| Url: {url}\n| Repeat: {rep}\n')

### get and set start time and date  ###
now=datetime.now(time_zone)
date_now=datetime.now()
date_now=now.strftime("%d. %m. %y")
current_time = now.strftime("%H:%M:%S")

###  program start   ###
print(f'[$] > ############################################################################################# \n[$] > #      PROGRAM HAS STARTED feel free to minimalize the window and go one with your day      #\n[$] > # When you wish to see the data in your txt file come back to this window and press \"crl+c\" #\n[$] > ############################################################################################# ')

###   write to file time and date of when program started  ###
file_.write(f'[$] > #Program started on {date_now} at {current_time} #\n')


while True:
    ###  get current time and date  ###
    now=datetime.now(time_zone)
    date_now=datetime.now()
    date_now=now.strftime("%d. %m. %y")
    current_time = now.strftime("%H:%M:%S")
    print("-----------------------")
    print(f'[log] Current Time = {current_time} | Current Date = {date_now}')
    ###  try astablish connection with the site  ###
    try:
        request=requests.get(url=url,timeout=5)
        print("[log] connection successful")

    ###  if you cant connect because of connection error  ###
    except(requests.ConnectionError, requests.Timeout) as exeption:
        ###  get current time and date  ###
        a=datetime.now()
        ###  write to file when the connection couldnt be made  ###
        file_.write(f'[!] Unable to connect [connection error] at {current_time}        | {date_now} | [!]\n')
        print("[log] unable to connect")
    print("-----------------------")
    time.sleep(rep)
