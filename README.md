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

Tor-Enabled Version
=====

(Documentation incomplete)

For the Tor-enabled version of SUMAC, there are a few dependencies.

1. Tor (duh!): You can find tutorials on OS-specific Tor installation around the web. Check https://torproject.org

2. stem: `pip install stem` should work, it is a python module for controlling Tor through a Python script. Necessary for changing IPs between checks. If you do not have pip installed, the package name for it should be `python-pip`.

3. requesocks: `pip install requesocks` should do the trick; similar to "requests", except allows for socks5 proxy. Necessary for Tor to make connections.

4. Configuration: Here is a sample configuration for Tor: https://pod.so/?8e4b1f136b07f74a#TsACK1KlgU9pY45oX33w8mFOHXLg/p5U7hNe08cu1qU=
This shows the lines that should be uncommented. If anything else is running on Tor, just be sure these values are set (or changed in the script). Make sure cookie authentication is enabled.

5. A decent understanding of Tor (a.k.a. not spamming issues "why is it not a stable 1 check per second?!? wtf?!?")
