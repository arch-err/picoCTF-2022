#!/usr/bin/env zsh
#!CMD: ./solve.sh

for i in $(seq 0 9)
do
	printf "$i\n"
	time echo "$i"000000 | ./pin_checker >/dev/null
	# time echo 48390513 | ./pin_checker >/dev/null
done
