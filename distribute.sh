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

let "triger=tutors/remainder - 1"
const=${triger}

echo triger is ${triger}

track=0

if [ ! -e ${basedir}${array[${track}]}/${pa}_grading ]; then
	mkdir  ${basedir}${array[${track}]}/${pa}_grading
fi

count=0

for student in `ls ${pa}.turnin`; do
	cp -r ${pa}.turnin/${student} ${basedir}${array[${track}]}/${pa}_grading
	count=$((count+1))
	echo ${count}
	cd ${basedir}${array[${track}]}/${pa}_grading
	if [ `ls -1 | wc -l` -ge "$avg" ]; then
		if [["triger" -eq ]]; then
			
		elif [[ "$triger" -ne 1 ]]; then
			track=$((track + 1))
			if [ ! -e ${basedir}${array[${track}]}/${pa}_grading ]; then
				mkdir  ${basedir}${array[${track}]}/${pa}_grading
			fi
			echo ${array[${track}]}
			triger=$((triger-1))
		else 
			triger=${const}
		fi 
	fi 
	cd ${basedir}cs8af${collector}
done

echo avg psa is ${avg}
echo remainder is ${remainder}
echo total numebr of tutors is ${tutors}
