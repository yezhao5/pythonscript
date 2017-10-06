#author Ye Zhao 
#!/usr/bin/python
import os, os.path
import re, sys

def isDigit(s):
    return re.search("[^0-9]",s) is None
def isLetter(s):
    return re.search("[^a-z]",s) is None

dirs = os.listdir("/home/linux/ieng6/cs8af")
tutors = []
students = []
#look at these dirs
for dir_i in dirs:
    if (len(dir_i)>5) and (isDigit(dir_i[5])):
        tutors.append(dir_i)
    if (len(dir_i)>5) and (isLetter(dir_i[5])):
        students.append(dir_i);

print ("this many tutors:", len(tutors))
print ("this many students:", len(students))

#for traking which tutor
track = 0

path = ("/home/linux/ieng6/cs8af/"+"cs8af46/"+"psa0_grading")
os.mkdir (path);

