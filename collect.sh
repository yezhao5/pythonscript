#!/bin/bash

clas='cs8af'

if [ ! "$1" ]
then
    echo Usage: ${0} assn
    exit
fi

if [ ! -e ${1}.turnin ]
then
    mkdir ${1}.turnin
fi

for student in `ls ../ | grep "${clas}[a-z][a-z]"`
do
    if [ -e ../$student/..${1}.tar.gz ]
    then
	cp ../$student/..${1}.tar.gz ${1}.turnin/$student.${1}.tar.gz
    else
	echo $student did not submit ${1}
    fi
done

echo Collected files into ${1}.turnin
