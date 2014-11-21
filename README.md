# SUMAC
#### Skype User Mass Availability Checker

Usage: python sumac.py <wordlist>
The <wordlist> is, as the name suggests, a list of words that will be checked for availability.
The words should be seperated by newlines.

If you have a comma-seperated list, change `fcon_stripped.rstrip().split("\n")` on line 27 to `fcon_stripped.rstrip().split(",")`

### Dependencies

1. Tor (duh!): You can find tutorials on OS-specific Tor installation around the web. Check https://torproject.org

2. stem: `pip install stem` should work, it is a python module for controlling Tor through a Python script. Necessary for changing IPs between checks. If you do not have pip installed, the package name for it should be `python-pip`.

3. requesocks: `pip install requesocks` should do the trick; similar to "requests", except allows for socks5 proxy. Necessary for Tor to make connections.

4. Configuration: Here is a sample configuration for Tor:
https://pod.so/?dcce691a2c5a8709#Czsym7WXZCdDBrmh/T0rh5paCu5yWJ/yQAxrcZVxJtw=
This shows the lines that should be uncommented. If anything else is running over Tor on the machine, you don't need to clear it, just be sure these values are set (or changed in the script). Make sure cookie authentication is enabled.

5. A decent understanding of Tor (a.k.a. not spamming issues "why is it not a stable 1 check per second?!? wtf?!?")
