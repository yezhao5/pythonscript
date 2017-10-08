#!/usr/bin/python

import os, sys
import csv

### VARS
# cse30
clas = 'cs30x'
serv = 'ieng9'

# cse11
#clas = 'cs11f'
#serv = 'ieng6'
### END VARS

if(len(sys.argv) < 2):
    print "Usage:", sys.argv[0], "assn"
    exit(1)

if(not os.path.isdir(sys.argv[1] + ".results")):
    print "Cannot find directory", sys.argv[1] + ".results"
    exit(1)

if(not os.path.isfile(sys.argv[1] + ".results/" + sys.argv[1] + ".csv")):
    print "Cannot find file", sys.argv[1] + ".results/" + sys.argv[1] + ".csv"
    exit(1)

skiprows = 0
maxcols = 0
rows = []
reader = csv.reader(open(sys.argv[1] + ".results/" + sys.argv[1] + ".csv", 'r'))
for row in reader:
    if(skiprows > 0):
        skiprows = skiprows - 1
        continue
    rows.append(row)
    if(len(row) > maxcols):
        maxcols = len(row)
print maxcols
for row in rows:
    if(len(row) < maxcols):
        for i in range(maxcols - len(row)):
            row.append("")
tuples = zip(*rows)

gsfile = open(sys.argv[1] + ".results/GRADESOURCE", 'w')
gsfile.write("[")
infocol = list(tuples[0])
infocol.pop(1)
for tuple in tuples[1:]:
    # Pop the grading status out
    tuple = list(tuple)
    tuple.pop(1)

    grader = tuple[0]
    student = tuple[1]
    totalscore = tuple[2]

    print student

    scorefile = open(sys.argv[1] + ".results/" + student + ".grade", "w")
    scorefile.write("DO NOT REPLY TO THIS EMAIL: If you have a question, please email the grader given below.\n")
    scorefile.write("REMEMBER: You have one week to resolve all grading issues related to this project.\n")
    for label, value in zip(infocol, tuple):
        # Rewrite grader label to email address
        if(label == "Grader" or label == "Tutor"):
            scorefile.write("Grader: " + clas + str(grader) + "@" + serv + ".ucsd.edu\n")
	elif (label.startswith("TOTAL") or label.startswith("README") or label.startswith("COMPILING") or 
		label.startswith("STYLE") or 
		label.startswith("CORRECTNESS") or label.startswith("EXTRA CREDIT")):
	    scorefile.write("\n"+label+ " " + value + "\n")
        else:
            scorefile.write(label + " " + value + "\n")

    os.system("finger -s -m " + student + " > " + sys.argv[1] + ".results/realname.file")
    scorefile.close()

    rnfile = open(sys.argv[1] + ".results/realname.file")
    s = rnfile.readline()
    s = rnfile.readline()
    fields = s.split()
    firstname = fields[1]
    lastname = fields[2]
    if(len(lastname) == 1):
        lastname = fields[3]
    lastname = lastname.replace("-", " ");
    gsfile.write("['" + firstname + "',")
    gsfile.write("'" + lastname + "',")
    gsfile.write(str(totalscore) + "],")
    rnfile.close()
gsfile.write("]")
gsfile.close()
print "Generated reports and placed in", sys.argv[1] + ".results"
