# Connection logger
Connection logger is a simple Python program that logs every time you are not 
connected to the internet.

## Requirements
To run this program you need to have:<br />
~ [Python](https://www.python.org/downloads/)<br />
> If you don't have package maneger such as pip (you shuld be fine using any other) installed you can follow thses steps to do so:<br />
  ~ [pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#:~:text=Download%20and%20Install%20pip%3A&text=Download%20the%20get%2Dpip.py,where%20the%20above%20file%20exists.&text=and%20wait%20through%20the%20installation,now%20installed%20on%20your%20system)

## Installation
1. In terminal move to the directory in which you have put your main.py and req.txt;
2. Use PIP to install required librarys:
> ```bash 
>pip install -r req.txt
>```

When the required librarys are installed you are ready to start the program :)
1. In terminal move to directiory where you have your main.py;
2. To start the program, in terminal write:
>```bash
>python main.py
>```
or
>```bash
>python3 main.py
>```
3. Now all the instructions you will need shuld be shown in your terminal

## PYTZ
[List for all available timezones for pytz library](https://github.com/us3-r/connection_logger/blob/main/pytz_timezone_list.py)

### Edit variubles
You can edit the following variubles:
```python
time_zone=pytz.timezone('') #<= put correct value for your time zone (see pytz_timezone_list.py to see correct values)
```
```python
url='https://blank.page/' #<= can change the url to any you want
```
```python
# amount of time it will wait before trying to connect to the site
refresh=10 #<= can change to any number ( refresh > 1) [in seconds]
```
