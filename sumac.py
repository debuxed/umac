#!/usr/bin/python

# Refer to LICENSE.txt in the Github repository to see how you can use this.
# Copyright (c) Dylan Hart 2014

try:
  import os
except ImportError:
  print "No os!"
try:
  import sys
except ImportError:
  print "No sys!"
try:
  import time
except ImportError:
  print "No time! *sprints away*"
try:
  import json
except ImportError:
  print "No json!"
try:
  import requesocks as requests
except ImportError:
  print "No requesocks!"
  print "try 'pip install requesocks'"
  print "Dependencies are listed in SUMAC's readme on Github!"
try:
  from stem import Signal
  from stem.control import Controller
except ImportError:
  print "No stem!"
  print "try 'pip install stem'"
  print "Dependencies are listed in SUMAC's readme on Github!"

print "\nSkype User Mass Availability Checker, a.k.a. SUMAC"
print "Created by Xeru [https://xeru.me]"
print "Experimental, report issues at https://github.com/exec/sumac/\n"
try:
    sys.argv[1]
except NameError:
    print "You must specify a wordlist!"
    print "Usage: " + sys.argv[0] + " <wordlist>"
except IndexError:
    print "You must specify a wordlist!"
    print "Usage: " + sys.argv[0] + " <wordlist>"
else:
    try:
        fname = sys.argv[1]
        fh = open(fname)
        fcon = fh.read()
        fcon_stripped = fcon.replace(" ", "")
        fcon_stripped = fcon_stripped.replace("\r", "")
        fcon_arr = fcon_stripped.rstrip().split("\n")
        if not os.path.exists('available-skype.txt'):
            open('available-skype.txt', 'w').close()
        print str(len(fcon_arr)) + " names loaded, and here we go!\n"
        for user in fcon_arr:
            with Controller.from_port(port = 9051) as controller: # Tor control port is defined here
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
            time.sleep(0.5)
            validator_url = "https://login.skype.com/json/validator?new_username=" + user
            validator_session = requests.session()
            validator_session.proxies = {'https': 'socks5://127.0.0.1:9050'}
            validator_response = validator_session.get(validator_url)
            validator_resptxt = validator_response.text
            validator_json_decoded = json.loads(validator_resptxt)
            validator_status = validator_json_decoded['status']
            if validator_status == 406:
                print user + " is taken"
            elif validator_status == 200:
                print user + " is available"
                with open("test.txt", "a") as availfile:
                    availfile.write(user + "\n")
            else:
                print user + " returned unknown status " + validator_status
            time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        print "\nSUMAC exiting: I am terminated"
