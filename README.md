# Raycast Commands

## Time-Converter
This command takes a time (local to your machine) as the first input, one or more comma-separated locations as the second input (optional), and a chosen format (optional). It will return the time in the locations using the format specified, or using the defaults.

### Examples
Examples typed in US Central Timezone:

*1.* `3PM` `NYC, London, Kolkata` `l`

"Output the times in New York City, London, and Kolkata that match 3PM my time (US Central) as a list"

Returns:
	
	```
	• 4:00 PM - NYC (US/Eastern)
	
	• 9:00 PM - London (UTC)
	
	• 2:30 AM - Kolkata (Asia/Kolkata)
	```



*2.* `3PM` `NYC, London, Kolkata` `i`
	
"Output the times in New York City, London, and Kolkata that match 3PM my time (US Central) inline"
	
Returns:
	
	
	`4:00 PM - NYC (US/Eastern) • 9:00 PM - London (UTC) • 2:30 AM - Kolkata (Asia/Kolkata)`


*3.* `10AM` (nothing else specified):

"Output the times for my default cities (Austin, TX, London, Sofia, Bulgaria) in the default format (bulleted list)"

Returns:
	
	
	```
	• 10:00 AM - Austin (US/Central)
	
	• 4:00 PM - London (UTC)
	
	• 6:00 PM - Sofia (Europe/Sofia)
	```


The command understands both 24-hour and 12-hour notation (the latter AM/PM or am/pm), with or without minutes as well as "fuzzy" times, such as "now" or "4PM tomorrow".

### Errors
The command does it's best to match input to timezones and most world capitals and major cities show up, but many cities will require using specific timezones. The command will highlight when it is unable to match - for example, the prompt `4pm` `Fort Worth` returns:

`• ‼️ No match: Fort Worth`

In this case, the better prompt would be `4pm` `US Central`.

### Setup Notes
Requires python 3.10+ which includes ZoneInfo and the match case statement. It also should have `pip3` installed by default, which is needed to install two supporting packages (see below).

There are three (easy) things that you'll need to do when you first use this command.
1. The first time you run this, you will be prompted to allow Raycast to access `System Events`, which is required in order for the command to paste the results.

	This script requires two additional python packages, both of which require that you use the Terminal (Terminal.app, which comes with macOS): 

2. [dateparser](https://dateparser.readthedocs.io/en/latest/):

 	`pip3 install dateparser`

3. applescript:

	`pip3 install applescript`

### Limitations
* Date ranges are not supported
* *This will replace your clipboard contents*. In order to paste the output, the script has to first copy the output into the clipboard. Luckily, Raycast tracks the clipboard history.

### To-Do
- Disable copy-to-clipboard as it now pastes directly
- Add options or different scripts for:
	- single line output versus list
	- Copy to clipboard vs. paste
- Make a config where the user can include default locations, used if none are specified
- Add config to automatically include a specific location/time at the start or end of the string (a label for the input time)

### Credits & Acknowledgements
Inspired by the [Timezone Expander Alfred workflow](https://github.com/devonzuegel/timezone-expander.alfredworkflow) by [Devon Zuegel](https://devonzuegel.com)