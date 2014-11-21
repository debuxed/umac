sumac
=====

Skype User Mass Availability Checker

This is currently the first release of SUMAC.
Right now, searches are limited to one per 15 seconds, this is due to Microsoft's limitation on availability checks.
I will be adding Tor proxy support soon, which will allow for quicker checking. The original noproxy version will remain available, but is much slower.

Usage: python sumac.py <wordlist>
The <wordlist> is, as the name suggests, a list of words that will be checked for availability.
The words should be seperated by newlines.

If you have a comma-seperated list, change `fcon_stripped.rstrip().split("\n")` on line 27 to `fcon_stripped.rstrip().split(",")`

Tor-Proxy Version
=====

(Incomplete...) (Haven't even made the tor-proxy version yet...) (ayy...)

For the Tor-Proxy version of SUMAC, there are a few prerequisites.

1. stem: `pip install stem`, it is a python module for controlling Tor through a Python script. Necessary for changing IPs after every check. If you don't have pip installed, the package name for it should be `python-pip`.

2. Configuration: In lines with comments "CHANGEME", you must update values to reflect your Tor installation. This is currently only the Tor control port and passphrase. Both can be found in the /etc/tor/torrc file (or other Tor config file on non-n*x)

3. A decent understanding of Tor (a.k.a. not spamming issues "why is it not a stable 3 seconds per check?!? wtf?!?")
