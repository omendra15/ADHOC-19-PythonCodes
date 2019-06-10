#!/usr/bin/python3

#run in root..................


import subprocess
import os
import time

name = input("enter name of user to be added - ")
if name.isalpha() :
 print("creating user-------")

 password = 'Hello' + name
 os.system('sudo useradd -p $(openssl passwd -1 {}) {}'.format(password,name))
 time.sleep(2)
 print("user created successfully")


else :
 print("enter username having characters only")
