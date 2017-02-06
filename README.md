# UMAC
#### Username Mass Availability Checkers

Usage: `./umac.sh <skype/github/steam> <wordlist>`
Wordlist must be seperated by new lines only, no commas, etc.

If you have a comma-seperated list, change `fcon_stripped.rstrip().split("\n")` on line 27 to `fcon_stripped.rstrip().split(",")`

There may be false positives since the Tor network is not stable enough to guarantee all connecting IPs will be different. You should test all usernames before thinking they're available. No false-negatives will occur unless a Tor node fails and returns incorrect data (VERY VERY rare.)

### Dependencies for umac-skype.py

Since Skype works extra-hard to limit the number of name lookups you can do in a given time, we have to either abide by its limits (VERY slow) or use Tor (still slow, but not quite as bad). This brings in a few extra dependencies that the other scripts don't require.

1. Tor: You can find tutorials on OS-specific Tor installation around the web. Check https://torproject.org

2. stem: `pip install stem` should work, it is a python module for controlling Tor through a Python script. Necessary for changing IPs between checks. If you do not have pip installed and you don't know how to install it, lookup installing pip for python on your OS.

3. requesocks: `pip install requesocks` should do the trick; similar to "requests", except allows for socks5 proxy. Necessary for Tor to make connections.

4. Configuration: Some default values of the /etc/torrc file on Linux installations will need modification in order to work with SUMAC.

Please make sure the tor socks port is set to 9050 or the value of the socks5 port in the script is modified accordingly.

Please also make sure the control port is set to 9051 or the control port value in the script is modified accordingly.

Ensure that cookie authentication is enabled in your torrc file, in order for the script to be able to change identities (IPs).

These configuration changes should not cause issues with other uses of Tor; however, I would personally recommend leaving cookie authentication disabled when UMAC is not in use.

5. A decent understanding of Tor (a.k.a. not spamming issues "why is it not a stable 1 check per second?!? wtf?!?")

### License

UMAC - Username Mass Availability Checkers

Copyright (C) 2017  Dylan Hart (twitter.com/notxeru)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

A copy of this license is provided in the SUMAC GitHub
repository, in the root directory, under the filename "LICENSE".
