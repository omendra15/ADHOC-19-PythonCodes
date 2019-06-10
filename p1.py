#!/usr/bin/python3

#tells when you will turn 95

import datetime

name = input("enter your name")
age = int(input("your age  ? "))

x = int((95-age) +datetime.datetime.now().year)

print("you will turn 95 in %s." %(x))

