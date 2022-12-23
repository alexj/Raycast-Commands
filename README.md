# Raycast Commands
Understands 24 hour and 12 hour notation (requires AM/PM or am/pm), with or without minutes as well as "fuzzy" times, such as "4PM tomorrow"

# NOTES
Requires python 3.9+ which includes ZoneInfo
Requires [dateparser](https://dateparser.readthedocs.io/en/latest/):
 	`pip3 install dateparser`
 	Or, if you don’t have pip installed:
	`$ easy_install dateparser` 

# Limitations
* Raycast only allows three arguments at the moment, which means we can only allow one time and two locations, unless you fork/hardcode something different
* Date ranges are not supported


# To-Do
- Add string to clipboard or output to current app
- Determine if I can use two arguments, one for time and the other a comma-separated list of locations
- Automatically output the user's location at the end of the string
- Add arguments to accept location
- Add city name mapping for major locales
- Make a script config where the user can include default locations, used if none are specified
- Find a way to have Python scan a list of timezone names to match provided cities