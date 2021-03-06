# Connection logger
Connection logger is a simple Python program that logs every time you are not 
connected to the internet.

## Requirements
To run this program you need to have:<br />
~ [Python](https://www.python.org/downloads/)<br />
> If you don't have a package manager such as pip (you should be fine using any other) installed you can follow these steps to do so:<br />
  ~ [pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#:~:text=Download%20and%20Install%20pip%3A&text=Download%20the%20get%2Dpip.py,where%20the%20above%20file%20exists.&text=and%20wait%20through%20the%20installation,now%20installed%20on%20your%20system)

## Installation
1. In a terminal move to the directory in which you have put your main.py and req.txt;
2. Use PIP to install required libraries:
```bash 
pip install -r req.txt
```

## How to use

When the required libraries are installed you are ready to start the program :)
1. In a terminal move to the directory where you have your main.py;
2. To start the program, in terminal write:
```bash
python main.py -f -d -t -u -r
```
or
```bash
python3 main.py -f -d -t -u -r
```
or (in this case, default values will be used)
```bash
python3 main.py
```

>## What to put in arguments
>***arguments are optional; if you do not input your values then the default values will be used***
>```bash
>-f [file name] e.g.: test, conn_log
>```
>```bash
>-d [file directory] e.g.: C:\user\...
>```
>```bash
>-t [timezone] (see yours in pytz_timezone_list.py) e.g.: Europe/Ljubljana
>```
>```bash
>-u [url of the site] e.g.: https://www.google.com/
>```
>```bash
>-r [the time when program will try to reconnect to site] e.g.: 10
>```


## PYTZ
[List for all available timezones for pytz library](https://github.com/us3-r/connection_logger/blob/main/pytz_timezone_list.py)

## ISSUES
no issues for the current build
> [!] currently might not work on Windows since color functions have only been tested on Linux [ FIXED ]
