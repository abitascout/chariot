###############################################################################
# Names: Abdullah Alshamdayn, Joy Brown, Caitlin Burke, Samantha Gnagey
#        Robert Morton, Kyler Parker
# Group: The Chariot
# Date: 10/29/2021
# Assignment: Program 5: TimeLock
###############################################################################


from sys import stdin
from datetime import datetime, timezone
from time import time
from hashlib import md5
import pytz

INTERVAL = 60
#MANUAL_DATETIME = "2017 04 23 18 02 06"
MANUAL_DATETIME = ""

tz = pytz.timezone("America/Chicago")
date = input()
#print(date)

# print("year: " + year + " month: " + month + " day: " + day + " hour: " + hour + " minute: " + minute + " second:" + second)
if(MANUAL_DATETIME == ''):
    currentUTC = datetime.now(timezone.utc)
else:
    currentDateTime = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")
    #currentUTC = currentDateTime.replace(tzinfo=timezone.utc)
    currentUTC = currentDateTime.astimezone(pytz.UTC)

#print("current system time: {}".format(currentUTC))
#print()

epochDateTime = datetime.strptime(date, "%Y %m %d %H %M %S")

#print(epochDateTime)
epochUTC = tz.localize(epochDateTime)
epochUTC = epochDateTime.astimezone(pytz.UTC)
#print("epoch time: {}".format(epochUTC))

difference = currentUTC - epochUTC

#print(difference)

difference_in_sec = int(difference.total_seconds())

#print("seconds: {}".format(difference_in_sec))

difference_in_sec -= (difference_in_sec % INTERVAL)

#print("seconds: {}".format(difference_in_sec))
#print()

first_hash = md5(str(difference_in_sec).encode("ascii")).hexdigest()

#print(first_hash)

second_hash = md5(str(first_hash).encode("ascii")).hexdigest()

#print(second_hash)
#print()

hash_str = second_hash

code = ''
count = 0
for element in hash_str:
    if(not element.isnumeric()):
        if(count <= 1):
            code += element
            count += 1
            #print(element)
            
#print(code)

count = 0
for element in hash_str[::-1]:
    if(element.isnumeric()):
        if(count <= 1):
            code += element
            count += 1
            #print(element)
            
code += hash_str[len(hash_str)//2]
            
print("code: {}".format(code))