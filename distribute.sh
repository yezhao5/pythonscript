#!/bin/bash

if [ ! $1 ]; then
	echo "Error: Too Few Arguments"
	echo "Usage: $0 PA_NAME"
	exit 1
fi

pa="$1"

basedir=`pwd`
msdir="${basedir}/${pa}milestone.turnin"

mkdir -p ${pa}.results
cd ${pa}.turnin

final=0
ms=0
total=0

for student in `cat "${basedir}/students"`; do
	tarball="${student}.${pa}.tar.gz"
	if [ -e $tarball ]; then
		mkdir ${student}
		cd ${student}

		tar -zxf ../${tarball}
		cp "${basedir}/runTests.${pa}" ./runTests
		ms_mail="${msdir}/${student}/MILESTONE.MAIL"
		if [ -e $ms_mail ]; then
			cp "${ms_mail}" .
		fi

		final=$((final+1))
		total=$((total+1))
		cd ..
	fi

	if [ ! -d ${student} ] && [ -d "${msdir}/${student}" ]; then
		mkdir ${student}
		cd ${student}

		cp "${msdir}/${student}/MILESTONE.MAIL" .
		echo "Did Not Have a final turnin" >> SUMMARY.RESULTS

		ms=$((ms+1))
		total=$((total+1))
		chmod g+rw SUMMARY.RESULTS
		cd ..
	fi
done

echo "Processed ${pa}. total: ${total}, of which ${final} final turnins and ${ms} only milestones"
