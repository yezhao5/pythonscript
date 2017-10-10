#!/bin/bash

clas='cs8af'

pa="$1"
tutors=0
basedir="/home/linux/ieng6/cs8af/"

array=()

for tutor in `ls ../ | grep "${clas}[1-9]"`;
do
	rm -r ${basedir}${tutor}/${pa}_grading
done

