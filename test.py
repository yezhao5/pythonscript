#!/bin/bash
#getEmail.py
#Ye Zhao
import sys, os
import subprocess
import csv
import tempfile

account = 'cs8af46'

with tempfile.TemporaryFile() as tempf:
        sys.path.insert(0,'/home/linux/ieng6/cs8af/')
        proc = subprocess.Popen(['finger', account], stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = tempf.read()
        sys.path.insert(0,'/home/linux/ieng6/cs8af/cs8af46/')
        print(output)
        first = output.split()[3]
        last = output.split()[4]
first = str(first)
last = str(last)

first = first[2:len(first)-1]
last = last[2:len(last)-1]


print("\n\nfirst: "+first+"last: "+last)
name = "name"   
name = last+", "+first

print (name)

