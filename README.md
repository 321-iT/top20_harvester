# Usage

git clone https://github.com/321-iT/top20_harvester.git  
cd top20\_harvester

If not installed:

	pip3 install codingame
	pip3 install csv
	pip3 install sys

./harvest.sh "Contest handle" "output file name" (the .csv is added automatically)

example:
	./harvest.sh "22499132d096a88cf6d6bcdf606295e28bcd6c0" "round1"

The contest handle is the last number in the URL of the contest. Should be 39 characters long.
