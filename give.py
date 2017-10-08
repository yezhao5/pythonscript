#!/usr/bin/python
import os, sys
import math, random
from stat import *

### VARS
clas = "cs30x"
basedir = "/home/solaris/ieng9/cs30x/cs30x3/SPRING2017/"
#clas = "cs11f"

graders = None
#graders = [7]

### END VARS

if(len(sys.argv) < 2):
    print "Usage:", sys.argv[0], "assn"
    sys.exit(1)

if(not os.path.isfile(sys.argv[1] + ".blank.csv")):
    print "Did not find", sys.argv[1] + ".blank.csv"
    sys.exit(1)

f = open(sys.argv[1] + ".blank.csv")
tutors = f.readline().split(",")[1:-1] #[1:-1] to skip label and whitespace
status = f.readline()
students = f.readline().split(",")[1:-1] #[1:-1] to skip label and whitespace
f.close()

if(len(tutors) != len(students)):
    print "csv file corrupted?"
    print "tutor assignments:", len(tutors)
    print "students:", len(students)
    sys.exit(1)

for grader, student in zip(tutors, students):
    if graders != None and int(grader) not in graders:
        continue
    print 'Giving student', student, 'to grader', grader
    #os.mkdir('../../' + clas + str(grader) + / + sys.argv[1] + 'grading', 0770)
    #os.symlink(
    #print "mkdir -p ../../" + clas + str(grader) + "/" + sys.argv[1] + "grading"
    
    #print "ln -f -s `echo " + sys.argv[1] + ".turnin/" + student + "` ../../" + clas + str(grader) + "/" + sys.argv[1] + "grading"
    
    os.system("mkdir -p ../../" + clas + str(grader) + "/" + sys.argv[1] + "grading")
    #os.system("ln -fs " + basedir + "Helpers/convertZeroes.sh" + " ../../" + clas + str(grader) + "/" + sys.argv[1] + "grading")
    #os.system("ln -fs " + basedir + "Helpers/NEW_GRADER_README" + " ../../" + clas + str(grader) + "/" + sys.argv[1] + "grading")
    os.system("ln -fs " + basedir + sys.argv[1] + ".turnin/" + student + " ../../" + clas + str(grader) + "/" + sys.argv[1] + "grading")
    #os.system("ln -fs `echo `pwd``/" + sys.argv[1] + ".turnin/" + student + " ../../" + clas + str(grader) + "/" + sys.argv[1] + "grading")
    os.system("chmod -R g+rwx ../../" + clas + str(grader)+ "/" + sys.argv[1] + "grading")
    #os.system("rm -r ../../" + clas + str(grader) + "/" + sys.argv[1] + "grading/echo")
