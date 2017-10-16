#!/bin/bash
#getEmail.py
#Ye Zhao
#link student cse account with their name and emails

import sys, os
import subprocess
import csv
import tempfile


studList = []
#all students
studf = open('Roster - Sheet1.tsv', 'rU')
studNum = 0
for line in studf:
    if studNum == 0:
        studNum = studNum + 1
        continue;
    studNum = studNum + 1
    cells = line.rstrip('\n').split('\t')
    #append (Lastname, Firstname),email
    studList.append((cells[2], cells[7]))
stud = dict(studList)
studf.close()

#get Firstname Lastname from finger

col = 471
csvfile = open ('emailList.tsv', 'w')
csvfile.write("Account\tName\tEmail\n")

grading =  open('CSE8A PSA Grading - PA1.csv', encoding='utf-8')
mycsv = csv.reader(grading)
curline = 0
accounts = []
for j in mycsv:
    if curline == 2 :
        accounts = j[1:]
        #print(accounts)
    curline = curline + 1

for i in range (0, col):
    account = accounts[i]
    with tempfile.TemporaryFile() as tempf:
        sys.path.insert(0,'/home/linux/ieng6/cs8af/')
        proc = subprocess.Popen(['finger', account], stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = tempf.read()
        sys.path.insert(0,'/home/linux/ieng6/cs8af/cs8af46/')
        #print(output)
        if len(output.split()) < 6 :
            continue;
        first = output.split()[3]
        mid = output.split()[4]
        last = output.split()[5]
        mid = str(mid)

        first = str(first)
        last = str(last)
        
        mid = mid [2:len(mid)-1]
        first = first[2:len(first)-1]
        last = last[2:len(last)-1]
        #print (last)
        name = last+", "+first+" "+ mid

        if last == "Directory:":
            
            name = mid+", "+first

        print (name)
    if name in stud:
        email = stud[name]
        csvfile.write(account+"\t"+name+"\t"+email+"\n")
    else:
        print("here.\n")
csvfile.close()
grading.close()
