# Raycast Commands
Understands 24 hour and 12 hour notation (requires AM/PM or am/pm), with or without minutes as well as "fuzzy" times, such as "4PM tomorrow"

# NOTES
Requires python 3.10+ which includes ZoneInfo and the match case statement
Requires [dateparser](https://dateparser.readthedocs.io/en/latest/):
 	`pip3 install dateparser`
 	Or, if you don’t have pip installed:
	`$ easy_install dateparser` 


# Limitations
* Raycast only allows three arguments at the moment, which means we can only allow one time and two locations, unless you fork/hardcode something different
* Date ranges are not supported


# To-Do
- Lowercase or title case the input and the list of timezones to improve fuzzy matching..?
- Add string to clipboard or output to current app
- Automatically output the user's location at the end of the string
- Add city name mapping for major locales
- Add separate lookup for matching against all timezones
- Make a script config where the user can include default locations, used if none are specified
- Find a way to have Python scan a list of timezone names to match provided cities