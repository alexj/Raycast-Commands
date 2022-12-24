# Raycast Commands
Understands 24 hour and 12 hour notation (requires AM/PM or am/pm), with or without minutes as well as "fuzzy" times, such as "4PM tomorrow".
Does it's best to match input to timezones. World capitals show up, but many cities will require using specific timezones

# NOTES
The first time you run this, you will be prompted to allow Raycast to access `System Events`, which is required in order for the command to paste the results.
Requires python 3.10+ which includes ZoneInfo and the match case statement
Requires [dateparser](https://dateparser.readthedocs.io/en/latest/):
 	`pip3 install dateparser`
 	Or, if you don’t have pip installed:
	`$ easy_install dateparser` 
Requires the applescript module
	`pip3 install applescript`

# Limitations
* Raycast only allows three arguments at the moment, which means we can only allow one time and two locations, unless you fork/hardcode something different
* Date ranges are not supported


# To-Do
- Output everything on one line
	- Perhaps an option for single line versus list output
- Add string to clipboard or output to current app
- Make a config where the user can include default locations, used if none are specified (Raycast doesn't support optional arguments)
- Add config to automatically include a specific location/time at the start or end of the string (a label for the input time)

# Credits
Inspired by the [Timezone Expander Alfred workflow](https://github.com/devonzuegel/timezone-expander.alfredworkflow) by [Devon Zuegel](https://devonzuegel.com)