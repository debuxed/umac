#!/usr/bin/python

# Refer to LICENSE.txt in the Github repository to see how you can use this.
# Copyright (c) Dylan Hart 2018

import os, sys, random, time, json

try:
  import requests
except ImportError:
  print "No requests package! Install with pip: pip install requests"
  sys.exit(1)

print "\nSTUMAC - Steam Username Mass Availability Checker  Copyright (C) 2017  Dylan Hart"
print "stumac.py comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law."
print "This is free software, and you are welcome to redistribute it under certain conditions."
print "View the 'LICENSE' file included in the STUMAC GitHub repository for more information.\n"
try:
    sys.argv[1]
except NameError:
    print "You must specify a wordlist!"
    print "Usage: ./umac.sh <skype/github/steam> <wordlist>"
except IndexError:
    print "You must specify a wordlist!"
    print "Usage: ./umac.sh <skype/github/steam> <wordlist>"
else:
    try:
        sys.argv[2]
    except NameError:
        silent = 'false'
    except IndexError:
        silent = 'false'
    else:
        silent = sys.argv[2]
    if silent == 'false':
        print "\033[92mGreen means available\033[0m"
        print "\033[91mRed means unavailable\033[0m\n"
    elif silent == 'av':
        print "\033[92mGreen means available\033[0m\n"
    elif silent == 'none':
        pass
    time.sleep(1)
    try:
        fname = sys.argv[1]
        fh = open(fname)
        fcon = fh.read()
        count = 0
        fcon_stripped = fcon.replace(" ", "")
        fcon_stripped = fcon_stripped.replace("\r", "")
        fcon_arr = fcon_stripped.rstrip().split("\n")
        if not os.path.exists('available-steam.txt'):
            open('available-steam.txt', 'w').close()
        print str(len(fcon_arr)) + " names loaded, and here we go!\n"
        if silent == "none":
            print "Silent mode enabled, username output will only be given to file.\n"
        elif silent == "av":
            print "Semi-silent mode enabled, only available usernames will be shown.\n"
            time.sleep(0.3)
        for user in fcon_arr:
            url = "https://steamcommunity.com/id/" + user
            session = requests.session()
            response = session.get(url)
            status = response.headers['content-length']
            if int(status) >= 5000:
                if silent == "av":
                    pass
                elif silent == 'false':
                    print "\033[91m" + user + "\033[0m (" + status + ")"
            elif int(status) <= 5000:
                resptext = response.text
                if resptext.find('<span class="actual_persona_name">') == -1:
                    if silent == "none":
                        pass
                    else:
                        print "\033[92m" + user + "\033[0m"
                    with open("available-steam.txt", "a") as af:
                        af.write(user + "\n")
                        af.close()
                else:
                    print "\033[91m" + user + "\033[0m (private)"
            else:
                print user + " returned unknown status " + status
    except (KeyboardInterrupt, SystemExit):
        print "\nSTUMAC exiting: I am terminated"
