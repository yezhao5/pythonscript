#!/bin/bash

### VARS
clas='cs30x'
### END VARS

if [ ! "$1" ]
then
    echo Usage: ${0} assn
    exit
fi

if [ ! -e ${1}.turnin ]
then
    mkdir ${1}.turnin
fi


#for student in `ls ../../ | grep "${clas}[a-x][a-z]"`
for student in `ls ../../ | grep "${clas}[a-x][a-z]"`
do
    if [ -e ../../$student/..${1}.tar.gz ]
    then
	cp -p ../../$student/..${1}.tar.gz ${1}.turnin/$student.${1}.tar.gz
    else
	echo $student did not submit ${1}
    fi
done

echo Collected files into ${1}.turnin
