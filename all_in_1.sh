#!/bin/bash

i=1
for var in $@
do
	python3 harvest.py $var round$i
	i=$((i+1))
done

python3 final_ranking.py ./round*
