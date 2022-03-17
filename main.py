
from calendar import c
from multiprocessing import connection
from os import path
import os
from datetime import datetime,date
import re
from timeit import repeat
from turtle import color
from numpy import full
import requests
from time import sleep
import time
import pytz
import argparse
from clr import colors

os.system("")
timeout=300

tzlist=[]
for time_ in pytz.all_timezones:
    tzlist.append(time_)

parser=argparse.ArgumentParser(description="commands")

parser.add_argument('-f', help="Name of your file",type=str,default="conn_log",)

parser.add_argument('-d',help="Name of your files directory",type=str,default=os.getcwd())

parser.add_argument('-t',help="your timezone",type=str,default='Europe/Ljubljana')

parser.add_argument('-u',help="url to desired website",type=str,default='https://blank.page/')

parser.add_argument('-r',help="time after which program will try to reconnect to the site",type=int, default=10)

args=parser.parse_args()
################### EXEPTIONS FOR ARG VALUES ###################
print("\n")

print(f"{colors.blue}▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀\n")
print("█▀▀ █▀█ █▄ █ █▄ █ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄ █\n█▄▄ █▄█ █ ▀█ █ ▀█ ██▄ █▄▄  █  █ █▄█ █ ▀█\n")
print("█   █▀█ █▀▀ █▀▀ █▀▀ █▀█\n█▄▄ █▄█ █▄█ █▄█ ██▄ █▀▄\n")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀")

### set file name

file_name1=args.f

### set file directory
file_path=""
fp=args.d
file_path=fp

state1="OK"
state2="OK"
state3="OK"
state4="OK"
state5="OK"
### set time zone
if args.t!=" ":
    timezon=args.t
    if timezon in tzlist:
        tz=timezon
    else:
        tz='Europe/Ljubljana'
        print(f'{colors.Lyellow}[!] Enterd timezone \"{timezon}\" is not in supported timezones; timezone is set to {tz} ')
        state3="W"
else:
    tz='Europe/Ljubljana'
    state3="W"

### url test
### sets deafult value for url
url='https://blank.page/'

### trys if the given url is working
if args.u!=url:
    url_=args.u
    try:
        request=requests.get(url_,timeout=10)
        url=args.u
    ### if the given url is not working it sets the url to default url
    except requests.exceptions.RequestException as ex:
        print(f'{colors.Lyellow}[!] There was an error with given url \"{args.u}\" new url is \"{url}\" ')
        url=url
        state4="W"
else:
    url=url
    state4="W"

### set repeat
new_r=args.r
if new_r<10:
    print(f'{colors.Lyellow}[!] For safety reasons this number shuld be bigger than 10 > so I set it to 10 :) \n')
    rep=10
    state5="W"
else:
    rep=args.r

################################################################

tz=tz
rep=float(rep)
time_zone=pytz.timezone(tz)


###  create file name and file path  ###
file_name=str(file_name1)
file_name=file_name1+".txt"
full_path=str(file_path+"/"+file_name)

###  open .txt file  ###
file_=open(full_path,"a")

### print all values  ###
print("\n")
if state1=="OK":
    print(f'{colors.green}[{state1}] File name: {file_name}')
else:
    print(f'{colors.Lyellow}[{state1}] File name: {file_name}')
if state2=="OK":
    print(f'{colors.green}[{state2}] File directory: {full_path}')
else:
    print(f'{colors.Lyellow}[{state2}] File directory: {full_path}')
if state3=="OK":
    print(f'{colors.green}[{state3}] Timezone: {tz}')
else:
    print(f'{colors.Lyellow}[{state3}] Timezone: {tz} | {colors.green}(OK)')
if state4=="OK":
    print(f'{colors.green}[{state4}] Url: {url} ')
else:
    print(f'{colors.Lyellow}[{state4}] Url: {url} | {colors.green}(OK)')
if state5=="OK":
    print(f'{colors.green}[{state5}] Repeat: {rep}\n')
else:
    print(f'{colors.Lyellow}[{state5}] Repeat: {rep} | {colors.green}(OK)\n')


### get and set start time and date  ###
now=datetime.now(time_zone)
date_now=datetime.now()
date_now=now.strftime("%d. %m. %y")
current_time = now.strftime("%H:%M:%S")

###  program start   ###
print(f'{colors.blue} ############################################################################################# \n #      PROGRAM HAS STARTED feel free to minimalize the window and go one with your day      #\n # When you wish to see the data in your txt file come back to this window and press \"crl+c\" #\n ############################################################################################# ')

###   write to file time and date of when program started  ###
file_.write(f'[$] > #Program started on {date_now} at {current_time} #\n')


while True:
    ###  get current time and date  ###
    now=datetime.now(time_zone)
    date_now=datetime.now()
    date_now=now.strftime("%d. %m. %y")
    current_time = now.strftime("%H:%M:%S")

    ###  try astablish connection with the site  ###
    try:
        request=requests.get(url=url,timeout=5)
        print(f"{colors.Dgray}-----------------------")
        print(f'{colors.Dgray}[log] Current Time = {current_time} | Current Date = {date_now}')
        print(f"{colors.Dgray}[log] connection succesfull")
    
    ###  if you cant connect because of connection error  ###
    except(requests.ConnectionError, requests.Timeout) as exeption:
        ###  get current time and date  ###
        a=datetime.now()
        ###  write to file when the connection couldnt be made  ###
        print(f"{colors.red}-----------------------")
        file_.write(f'[!] Unable to connect [connection error] at {current_time}        | {date_now} | [!]\n')
        print(f'{colors.red}[log] Current Time = {current_time} | Current Date = {date_now}')
        print(f"{colors.red}[log] unable to connect")
    
    time.sleep(rep)
