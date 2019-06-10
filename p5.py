#!/usr/bin/python3


import time

name = input("what`s your name - ")

time = int(time.strftime("%H"))

if time>=00 and time<=12 :
 print("good morning - ",name)

if time>12 and time<=17 :
 print("good afternoon - ",name)

if time>17 and time<=21 :
 print("good evening - ",name)

else :
 print("good night - ",name)

