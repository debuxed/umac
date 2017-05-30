# UMAC
#### Username Mass Availability Checkers

Usage: `./umac.sh <github/reddit/steam> <wordlist>`

Wordlist must be seperated by new lines only, no commas, etc.

If you have a comma-seperated list, change `fcon_stripped.rstrip().split("\n")` on line 27 to `fcon_stripped.rstrip().split(",")`

### License

UMAC - Username Mass Availability Checkers

Copyright (C) 2017  Dylan Hart (twitter.com/bumfucker)

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
