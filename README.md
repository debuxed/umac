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
