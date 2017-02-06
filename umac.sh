#!/bin/bash
if [ -z $1 ]; then echo "usage: ./umac.sh <skype/github/steam> <wordlist>"; else python $(dirname $0)/scripts/umac-$1.py $2; fi
