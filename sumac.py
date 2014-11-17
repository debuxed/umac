#!/usr/bin/python
import sys
import urllib2
import time
import json

# IMPORTANT SHIT READ
#
# Props to Skype for trying to prevent this by limiting request rate to their username availability check.
# Leave this checker running overnight in a 'screen', if you don't know what
# that is, look it up. It's slow to circumvent Microsoft's atttempt to block this.

print "Skype User Mass Availability Checker, a.k.a. SUMAC"
print "Created by Xeru [https://xeru.me]\n"
try:
    sys.argv[1]
except NameError:
    print "Usage: " + sys.argv[0] + " <wordlist>"
except IndexError:
    print "You must specify a wordlist!"
    print "Usage: " + sys.argv[0] + " <wordlist>"
else:
    fname = sys.argv[1]
    fh = open(fname)
    fcon = fh.read()
    fcon_stripped = fcon.replace(" ", "")
    fcon_stripped = fcon_stripped.replace("\r", "")
    fcon_arr = fcon_stripped.rstrip().split("\n")
    print fcon_arr
    print "List loaded"
    for user in fcon_arr:
        validator_url = "https://login.skype.com/json/validator?new_username=" + user
        validator_request = urllib2.Request(validator_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'})
        validator_response = urllib2.urlopen(validator_request).read()
        validator_json_decoded = json.loads(validator_response)
        validator_status = validator_json_decoded['status']
        if validator_status == 406:
            print user + " is taken"
        elif validator_status == 200:
            print user + " is available"
            availlist = open("available-skype.txt", "w+")
            availlist.write(user + "\n")
            availlist.close()
        else:
            print user + " returned unknown status " + validator_status
        time.sleep(15)
