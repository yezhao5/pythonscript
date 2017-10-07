#author Ye Zhao 
#!/usr/bin/python

import os, os.path
import re, sys
import pxssh

#constants
CONST_DIR_AF = "/home/linux/ieng6/cs8af/"
CONST_GRADE_DIR = "/psa0_grading/"
CONST_TAR = "/psa0.gz.tar"
CONST_ST_SCP_PATH = "@ieng9.ucsd.edu:psa0/psa0.gz.tar"
CONST_TU_SCP_PATH = "@ieng9.ucsd.edu:psa0_grading/"

def isDigit(s):
    return re.search("[^0-9]",s) is None
def isLetter(s):
    return re.search("[^a-z]",s) is None

log = None

def login(s):
    log = pxssh.pxssh()
    if not:
        print ("ssh failed with "+ s)
        return False 
    else:
        print ("ssh success with " +s)
        

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
triger = len(tutor)/reminder + 1
TRIGER = triger

for x in students
        #create stud folder
        path = (CONST_DIR_AF + tutors[track]+CONST_GRADE_DIR+student[x])
        os.mkdir (path)    
        #scp    
        log.sendline("scp "+student[x]+ CONST_SU_SCP_PATH + tutors[track]+CONST_TU_SCP_PATH + students[x])
        #tar
        log.sendline("tar xfvz " + CONST_DIR_AF + tutors[track]+"/"+students[x]+CONST_TAR)
        count = os.listdir(CONST_DIR_AF+tutors[track])
        if (len(count)>avg):
            if not triger = 1:
                track = track +1
                log.logout()
                login(tutors[track])
                path = (CONST_DIR_AF + tutors[track] + CONST_GRADE_DIR)
                log.sendline("makir "+ path)
                triger = triger-1
            else: 
                triger = TRIGER
