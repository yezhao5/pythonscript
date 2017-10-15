#!/bin/bash
#getEmail.py
#Ye Zhao
#link student cse account with their name and emails

import sys, os
import subprocess
import csv

studList = []
#student account from grading sheet
studList = open('Roster - Sheet1.tsv', 'rU')
for line in studList:
    cells = line.rstrip('\n').split('\t')
    #append (Lastname, Firstname),email
    studList.append((cells[2], cells[7]))
stud = dict(studList)
print len(roster)

#get Firstname Lastname from finger

col = 473
csvfile = open ('emailList.csv', 'w')
csvfile.write("Account,Name,Email\n")

grading =  open('CSE8A PSA Grading - PA1.csv')
mycsv = csv.reader(grading)
mycsv = list (mycsv)
lineNumber = 2
readCol = 0
for i in range (0, col)
    account = mycsv[lineNumber][i]
    csvfile.write(account+',')
    readCol = readCol+1
    
    first = 'a'
    last = 'a'

    with tempfile.TemporaryFile() as tempf:
        sys.path.insert(0,'/home/linux/ieng6/cs8af/')
        proc = subprocess.Popen(['finger', account], stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = tempf.read()
        print(output)
        name = output.split('Name:')[1]
        name = name.split('Directory:')[0]
        first, last = s.split
    print("first: "+first+"last: "+last)
    
    name = last+", "first

    print name
    email = stud[name]

    csvfile.write(name+','+email+'\n')
csvfile.close()
