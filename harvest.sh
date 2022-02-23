#!/bin/bash

rm output &>/dev/null

python3 harvest.py $1 > output
cat output | head -n 20
rm output &>/dev/null
