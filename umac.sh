#!/bin/bash
if [ -z $1 ]; then echo "usage: ./umac.sh <github/reddit/steam> <wordlist>"; else python $(dirname $0)/scripts/umac-$1.py $2; fi
