# SUMAC
#### Skype User Mass Availability Checker

Usage: python sumac.py <wordlist>
The <wordlist> is, as the name suggests, a list of words that will be checked for availability.
The words should be seperated by newlines.

If you have a comma-seperated list, change `fcon_stripped.rstrip().split("\n")` on line 27 to `fcon_stripped.rstrip().split(",")`

There may be false positives since the Tor network is not stable enough to guarantee all connecting IPs will be different. You should test all usernames before thinking they're available. No false-negatives will occur unless a Tor node fails and returns incorrect data (VERY VERY rare.)

### Dependencies

1. Tor: You can find tutorials on OS-specific Tor installation around the web. Check https://torproject.org

2. stem: `pip install stem` should work, it is a python module for controlling Tor through a Python script. Necessary for changing IPs between checks. If you do not have pip installed and you don't know how to install it, lookup installing pip for python on your OS.

3. requesocks: `pip install requesocks` should do the trick; similar to "requests", except allows for socks5 proxy. Necessary for Tor to make connections.

4. Configuration: Some default values of the /etc/torrc file on Linux installations will need modification in order to work with SUMAC.

Please make sure the tor socks port is set to 9050 or the value of the socks5 port in the script is modified accordingly.

Please also make sure the control port is set to 9051 or the control port value in the script is modified accordingly.

Ensure that cookie authentication is enabled in your torrc file, in order for the script to be able to change identities (IPs).

These configuration changes should not cause issues with other uses of Tor; however, I would personally recommend leaving cookie authentication disabled when SUMAC is not in use.

5. A decent understanding of Tor (a.k.a. not spamming issues "why is it not a stable 1 check per second?!? wtf?!?")
