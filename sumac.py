#!/usr/bin/python

# Refer to LICENSE.txt in the Github repository to see how you can use this.
# Copyright (c) Dylan Hart 2015

import os, sys, random

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
print "\nSUMAC - Skype Username Mass Availability Checker  Copyright (C) 2015  Dylan Hart"
print "sumac.py comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law."
print "This is free software, and you are welcome to redistribute it under certain conditions."
print "View the 'LICENSE' file included in the SUMAC GitHub repository for more information.\n"
try:
    sys.argv[1]
except NameError:
    print "You must specify a wordlist!"
    print "Usage: " + sys.argv[0] + " [-d] <wordlist>"
except IndexError:
    print "You must specify a wordlist!"
    print "Usage: " + sys.argv[0] + " [-d] <wordlist>"
else:
    try:
        fname = sys.argv[1]
        fh = open(fname)
        fcon = fh.read()
        count = 0
        fcon_stripped = fcon.replace(" ", "")
        fcon_stripped = fcon_stripped.replace("\r", "")
        fcon_arr = fcon_stripped.rstrip().split("\n")
        if not os.path.exists('available-skype.txt'):
            open('available-skype.txt', 'w').close()
        print str(len(fcon_arr)) + " names loaded, and here we go!\n"
        for user in fcon_arr:
            validator_url = "https://login.skype.com/registration/validator"
            validator_session = requests.session()
            validator_session.proxies = {'https': 'socks5://127.0.0.1:9050'}
            validator_payload = "skypename="+user
            validator_response = validator_session.post(validator_url, headers={"Origin":"https://login.skype.com","Accept":"application/json, text/javascript","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"}, data=validator_payload)
            validator_resptxt = validator_response.text
            validator_json_decoded = json.loads(validator_resptxt)
            validator_status = validator_json_decoded['status']
            validator_status_code = validator_status['code']
            if validator_status_code == 40601:
                print user + " is \033[91mtaken\033[0m [\033[91m" + str(validator_status_code) + "\033[0m]"
            elif validator_status_code == 20000:
                print user + " is \033[92mavailable\033[0m [\033[92m" + str(validator_status_code) + "\033[0m]"
                with open("available-skype.txt", "a") as availfile:
                    availfile.write(user + "\n")
                    availfile.close()
            else:
                print user + " returned unknown status"
            if not count % 4:
                with Controller.from_port(port = 9051) as controller: # Tor control port is defined here
                    controller.authenticate()
                    controller.signal(Signal.NEWNYM)
                time.sleep(9.2)
            count = count + 1
            time.sleep(0.3)
    except (KeyboardInterrupt, SystemExit):
        print "\nSUMAC exiting: I am terminated"
