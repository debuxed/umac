sumac
=====

Skype User Mass Availability Checker

This is currently the first release of SUMAC.
Right now, searches are limited to one per 15 seconds, this is due to Microsoft's limitation on availability checks.
I will be adding proxy support soon, which will allow for much quicker checking. For now this is it.

Usage: python sumac.py <wordlist>
The <wordlist> is, as the name suggests, a list of words that will be checked for availability.
The words should be seperated by newlines.

If you have/prefer a comma-seperated list you can change `fcon_stripped.rstrip().split("\n")` on line 27 to `fcon_stripped.rstrip().split(",")`
