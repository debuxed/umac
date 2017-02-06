#!/bin/bash
if [ -z $1 ]; then echo "usage: ./umac.sh <skype/github/steam>"; else python $(dirname $0)/scripts/umac-$1.py; fi
