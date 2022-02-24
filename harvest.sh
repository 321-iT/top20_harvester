#!/bin/bash

rm output &>/dev/null

python3 harvest.py $1 $2 > output
cat output
rm output &>/dev/null
