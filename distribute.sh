#!/bin/bash

clas='cs8af'

pa="$1"
turnins="$2"
collector="$3"
tutors=0
basedir="/home/linux/ieng6/cs8af/"

array=()

for tutor in `ls ../ | grep "${clas}[1-9]"`;
do
    	array+=(${tutor})
    	tutors=$((tutors+1))
done

let "avg=turnins/tutors"
let "remainder=turnins%tutors"

track=0

if [ ! -e ${basedir}${array[${track}]}/${pa}_grading ]; then
	mkdir  ${basedir}${array[${track}]}/${pa}_grading
fi



OUTPUT=$(python ./randomArray.py ${remainder})

count=0

for student in `ls ${pa}.turnin`; do
	cp -r ${pa}.turnin/${student} ${basedir}${array[${track}]}/${pa}_grading
	count=$((count+1))
	cd ${basedir}${array[${track}]}/${pa}_grading
	if [ `ls -1 | wc -l` -ge "$avg" ]; then
		exist=0
		for extra in $OUTPUT; do
			if [[ ${array[${track}]} -eq ${extra} ]]; then
				exist=1
				break
			fi
		done
		
		if [ "$exist" -eq 1 ]; then
			if [ `ls -1 | wc -l` -gt "$avg" ]; then			
				track=$((track + 1))
				if [ ! -e ${basedir}${array[${track}]}/${pa}_grading ]; then
					mkdir  ${basedir}${array[${track}]}/${pa}_grading
				fi
			fi
		else
			track=$((track + 1))
			if [ ! -e ${basedir}${array[${track}]}/${pa}_grading ]; then
				mkdir  ${basedir}${array[${track}]}/${pa}_grading
			fi	
		fi
	fi 
	cd ${basedir}cs8af${collector}
done




echo avg psa is ${avg}
echo remainder is ${remainder}
echo total numebr of tutors is ${tutors}
