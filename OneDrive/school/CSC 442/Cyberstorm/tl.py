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

if(MANUAL_DATETIME == ''):
    currentUTC = datetime.now(timezone.utc)
else:
    currentDateTime = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")
    currentUTC = currentDateTime.astimezone(pytz.UTC)


epochDateTime = datetime.strptime(date, "%Y %m %d %H %M %S")

epochUTC = tz.localize(epochDateTime)
epochUTC = epochDateTime.astimezone(pytz.UTC)

difference = currentUTC - epochUTC

difference_in_sec = int(difference.total_seconds())

difference_in_sec -= (difference_in_sec % INTERVAL)

first_hash = md5(str(difference_in_sec).encode("ascii")).hexdigest()

second_hash = md5(str(first_hash).encode("ascii")).hexdigest()

hash_str = second_hash

code = ''
count = 0
for element in hash_str:
    if(not element.isnumeric()):
        if(count <= 1):
            code += element
            count += 1

count = 0
for element in hash_str[::-1]:
    if(element.isnumeric()):
        if(count <= 1):
            code += element
            count += 1
            
            
###################################################################################
# UNCOMMENT AND MODIFY FOLLOWING LINE TO ADD A FIFTH CHARACTER TO THE FINAL CODE            
# code += hash_str[len(hash_str)//2]
###################################################################################
            
print("code: {}".format(code))