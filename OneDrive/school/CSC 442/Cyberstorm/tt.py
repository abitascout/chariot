from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdout


sleep(8)

features = ['A', 'r', 'e', ' ', 'y', 'o', 'u', ' ', 'f', 'r', 'u', 's', 't', 'r', 'a', 't', 'e', 'd', ' ', 'o', 'r', ' ', 'e', 'x', 'c', 'i', 't', 'e', 'd', '?', 'Ar', 're', 'e ', ' y', 'yo', 'ou', 'u ', ' f', 'fr', 'ru', 'us', 'st', 'tr', 'ra', 'at', 'te', 'ed', 'd ', ' o', 'or', 'r ', ' e', 'ex', 'xc', 'ci', 'it', 'te', 'ed', 'd?']

times = ['0.36', '0.67', '0.59', '0.49', '0.97', '0.54', '0.80', '0.19', '0.14', '0.67', '0.97', '0.39', '0.48', '0.61', '0.35', '0.99', '0.31', '0.92', '0.50', '0.49', '0.58', '0.55', '0.97', '0.88', '0.30', '0.63', '0.26', '0.62', '0.94', '0.38', '0.31', '0.33', '0.51', '0.90', '0.13', '0.56', '0.74', '0.93', '0.54', '0.74', '0.24', '0.66', '0.57', '0.98', '0.89', '0.14', '0.75', '0.24', '0.21', '0.44', '0.53', '0.68', '0.61', '0.48', '0.71', '0.41', '0.17', '0.15', '0.29']

#debug
DEBUG = True 
password = features
timings = times
if DEBUG == True:
    print(f'Features = {password}')
    print(f'Timings = {timings}')
#gets the password

password = password[:len(password)//2 +1]
password ="".join(password)
if DEBUG == True:
    print(f'Sample = \"{password}\"')
#gets the timings

timings = [float(a) for a in timings ]
keypress = timings[:len(timings)//2 +1]
keyintervals = timings[len(timings)//2 +1:]
if DEBUG == True:
    print(f'KHTs = {keypress}')
    print(f'KITs = {keyintervals}')

keyboard = Controller()

string = password
i = 0
j = 0
#prints out the string using the keypress and keyintervals
for char in string:
    keyboard.press(char)
    sleep(keypress[i])
    keyboard.release(char)
    sleep(keyintervals[j])
    i+=1
    j+=1
    

tcflush(stdout, TCIFLUSH)


