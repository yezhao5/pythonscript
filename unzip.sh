#!/bin/bash
if [ ! $1 ]; then
	echo "Error: Too Few Arguments"
	exit 1
fi

clas='cs8af'
pa="$1"

cd ${pa}.turnin

total=0
for student in `ls ../../ | grep "${clas}[a-z][a-z]"` 
do
	tarball="${student}.${pa}.tar.gz"
	if [ -e $tarball ]; then
		mkdir ${student}
		cd ${student}
		tar -zxf ../${tarball}
		total=$((total+1))
		cd ..
		mv ${tarball} ../tars
	fi


done

for student in `ls ../../ | grep "${clas}[a-z][a-z][a-z]"` 
do
	tarball="${student}.${pa}.tar.gz"
	if [ -e $tarball ]; then
		mkdir ${student}
		cd ${student}
		tar -zxf ../${tarball}
		total=$((total+1))
		cd ..
		mv ${tarball} ../tars
	fi


done

echo "Processed ${pa}. total: ${total} turnins"
