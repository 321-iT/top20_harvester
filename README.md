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
		will output the top 20, and put the result in 'round1.csv'

The contest handle is the last number in the URL of the contest. Should be 39 characters long.

To add later :
	- "map" that is used to transform pseudo into logins based on manually done configuration file
	- on the same basis, adds in csv output a field corresponding to the number of points
	- create a script that takes multiple .csv files and agregate them into one (maybe this already exist) in order to produce the final ranking (to do this i need the third "score" field in all rounds.csv outputs, and a configuration file that indicates a number of points for each place in the ranking)
