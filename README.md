# Usage

	git clone https://github.com/321-iT/top20_harvester.git  
	cd top20\_harvester

If not installed:

	pip3 install codingame
	pip3 install csv
	pip3 install sys

To launch the script:

	python3 harvest.py "Contest handle" "output file name" (the .csv is added automatically)

The contest handle is the last part of the URL of the contest. Should be 39 characters long.

Example:

>python3 harvest.py "22499132d096a88cf6d6bcdf606295e28bcd6c0" "round1"

This command will output the top 20, and put the result in 'round1.csv'


It is possible to add points for each place in the ranking.
In order to do this you have to use or create "score.cfg".

"score.cfg" is formatted as below:

It <strong>has</strong> to be formatted like this:

	//place,points
	1,100
	2,90
	3,80
	...

On the exact same basis, you have the pseudo.cfg to map a CodinGame pseudo to a login.

It <strong>has</strong> to be formatted the same way:

	//CodinGame Pseudo, login
	lmartinUwU,lmartin
	dArkGam3rxXx,nfascia
	lostarkaddict,pdubois
	...

Once you have finished all rounds, you have a final script   (final_ranking.sh) that will take all the "roundsX.csv" files and produce one final ranking based on the score of each person for each round.

You can launch it like this:

	python3 final_ranking.py round1.csv round2.csv round3.csv [...] roundN.csv
