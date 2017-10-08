#!/usr/bin/python

import os, sys
import math, random
from stat import *
import itertools

### VARS
# CSE30
clas = 'cs30x'
graders = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]
#graders = [1]
### END VARS

if(len(sys.argv) < 2):
    print "Usage:", sys.argv[0], "assn"
    sys.exit(1)

submissions = []

files = os.listdir(sys.argv[1] + ".turnin")
for file in files:
    if(os.path.isdir(sys.argv[1] + ".turnin/" + file)):
        submissions.append(file)
    
perperson = int(math.ceil(len(submissions) / float(len(graders))))

assigns = []
while(len(assigns) < len(submissions)):
    gradersx = list(graders)
    random.shuffle(gradersx)
    assigns.extend(gradersx)
assigns = assigns[0:len(submissions)]
final_list = zip(assigns, submissions)
final_list.sort()

#assigns = []
#for grader in graders:
#    stuff = itertools.repeat(grader, perperson)
#    for L in stuff:
#        assigns.append(L)
#random.shuffle(assigns)
##final_list = sorted(zip(assigns, students))
#final_list = zip(assigns, submissions)
#final_list.sort()

csvfile = open(sys.argv[1] + ".blank.csv", 'w')
csvfile.write("Grader,")
for (grader, student) in final_list:
    csvfile.write(str(grader) + ",")
csvfile.write("\nStatus,")
for (grader, student) in final_list:
    csvfile.write("N,")
csvfile.write("\n" + clas + " Student,")
for (grader, student) in final_list:
    csvfile.write(student + ",")
csvfile.write('\n')

# Open guidelines
guide = open('Helpers/' + sys.argv[1] + '.gradetemplate', 'r')
lines = guide.readlines()
for line in lines:
    csvfile.write(line)

# Open autograde testcases if any
#if(os.path.isdir('Helpers/' + sys.argv[1] + '.tests')):
#    files = (os.listdir('Helpers/' + sys.argv[1] + '.tests'))#.sort()
#    listfiles = []
#    for file in files:
#        if(file.find(".test") != -1):
#            listfiles.append(file)
#    listfiles.sort()
#    for file in listfiles:
#        csvfile.write(file + ':\n')
#    csvfile.write("Comments:\n")

csvfile.close()
print "%d students were assigned (%d per grader)" % (len(final_list), perperson) 
print "Generated " + sys.argv[1] + ".blank.csv file"
