# Usage

git clone https://github.com/321-iT/top20_harvester.git  
cd top20\_harvester

If not installed:

	pip3 install codingame
	pip3 install csv
	pip3 install sys

./harvest.sh "Contest handle" "output file name" (the .csv is added automatically)

The contest handle is the last part of the URL of the contest. Should be 39 characters long.

Example:

>./harvest.sh "22499132d096a88cf6d6bcdf606295e28bcd6c0" "round1"

This command will output the top 20, and put the result in 'round1.csv'


If you want to add points in the final ranking, in order to do this you have to create "points.cfg".


It *has* to be formatted like this:

//PLACE, POINTS
1,100
2,90
3,80
...

On the exact same basis, you have the pseudo.cfg to map a CodinGame pseudo to a login.

It *has* to be formatted the same way:

//CodinGame Pseudo, login
lmartinUwU,lmartin
dArkGam3rxXx,nfascia
lostarkaddict,pdubois
...
