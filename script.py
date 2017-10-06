#author Ye Zhao 
#!/usr/bin/python
import os, os.path
import re, sys
import pxssh

#constants
CONST_DIR_AF = "/home/linux/ieng6/cs8af/"
CONST_GRADE_DIR = "/psa0_grading/"
CONST_TAR = "/psa0.gz.tar"
CONST_STUD_EMAIL_PATH = "@ieng9.ucsd.edu:psa0/psa0.gz.tar"
CONST_TUR_EMAIL_PATH = "@ieng9.ucsd.edu:psa0_grading/"

def isDigit(s):
    return re.search("[^0-9]",s) is None
def isLetter(s):
    return re.search("[^a-z]",s) is None

dirs = os.listdir(CONST_DIR_AF)
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

track = 0

login(tutors[track])
path = (CONST_DIR_AF+tutors[track]+CONST_GRADE_DIR)
os.mkdir (path);

hw_count = 0

for x in students:
    path = (CONST_DIR_AF + students[x] + CONST_TAR)
    check = os.path.isfile(path)
    if check:
        hw_count = hw_count+1
    else:
        students.remove(students[x])


avg = len(students)/len(tutors)
reminder = len(students) - (avg* len(tutors))

for x in students
        #create stud folder
        path = (CONST_DIR_AF + tutors[track]+CONST_GRADE_DIR+student[x])
        os.mkdir (path)    
        #scp    
        os.system("scp "+student[x]+ CONST_SUTD_EMAIL_PATH + tutors[track]+CONST_TUR_EMAIL_PATH + students[x])
        #tar
        os.system("tar xfvz " + CONST_DIR_AF + tutors[track]+"/"+students[x]+CONST__TAR)
        count = os.listdir(CONST_DIR_AF+tutors[track])
        if (len(count)>avg):
            track = track +1
            login(tutors[track])
            path = (CONST_DIR_AF + tutors[track] + CONST_GRADE_DIR)
            os.makir (path)
        os.makir (path)
