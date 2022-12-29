# Raycast Time-Converter Command
This command takes a time (local to your machine) and one or more locations and returns the time in the specified locations. For example (typed in US Central Timezone):
	`3PM | NYC, London, Kolkata`
returns
	`• 4:00 PM - NYC (US/Eastern)
	• 9:00 PM - London (UTC)
	• 2:30 AM - Kolkata (Asia/Kolkata)
`

Understands 24 hour and 12 hour notation (requires AM/PM or am/pm), with or without minutes as well as "fuzzy" times, such as "now" or "4PM tomorrow" .
Does it's best to match input to timezones. World capitals show up, but many cities will require using specific timezones

# NOTES
The first time you run this, you will be prompted to allow Raycast to access `System Events`, which is required in order for the command to paste the results.
Requires python 3.10+ which includes ZoneInfo and the match case statement

Requires [dateparser](https://dateparser.readthedocs.io/en/latest/):

 	`pip3 install dateparser`
 	
Or, if you don’t have pip installed:
 	
	`$ easy_install dateparser` 
	
Requires the applescript module:

	`pip3 install applescript`

# Limitations
* Date ranges are not supported
* See the items in the To-Do section below, which highlight some potential options


# To-Do
- Disable copy-to-clipboard as it now pastes directly
- Perhaps an option or different script for:
	- single line versus list output
	- Copy to clipboard vs. paste
- Make a config where the user can include default locations, used if none are specified (Raycast doesn't support optional arguments)
- Add config to automatically include a specific location/time at the start or end of the string (a label for the input time)

# Credits
Inspired by the [Timezone Expander Alfred workflow](https://github.com/devonzuegel/timezone-expander.alfredworkflow) by [Devon Zuegel](https://devonzuegel.com)