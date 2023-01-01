# Raycast Commands

## Time-Converter
This command takes a time (local to your machine) as the first input, one or more comma-separated locations as the second input (optional), and a chosen format (optional). It will return the time in the locations using the format specified, or using the defaults.

### Examples
Examples typed in US Central Timezone:

*1.* `3PM` `NYC, London, Kolkata` `l`

"Output the times in New York City, London, and Kolkata that match 3PM my time (US Central) as a list"

Returns:
	
```
• 4:00 PM - NYC
• 9:00 PM - London
• 2:30 AM - Kolkata

```


*2.* `3PM` `NYC, London, Kolkata` `inline`
	
"Output the times in New York City, London, and Kolkata that match 3PM my time (US Central) inline"
	
Returns:
	
	
`4:00 PM NYC / 9:00 PM London / 2:30 AM Kolkata`


*3.* `10AM` (nothing else specified):

"Output the times for the default cities (Austin, TX, London, Sofia, Bulgaria -- see below for how you can change these) in the default inline format

Returns:
	
	
```
10:00 AM Austin / 4:00 PM London / 6:00 PM Sofia
```


The command understands both 24-hour and 12-hour notation (the latter AM/PM or am/pm), with or without minutes as well as "fuzzy" times, such as "now" or "4PM tomorrow".

### Limitations
* Date ranges are not supported
* *This will replace your clipboard contents*. In order to paste the output, the script has to first copy the output into the clipboard. Luckily, Raycast tracks the clipboard history.

### Errors
The command does it's best to match input to timezones and most world capitals and major cities show up, but many cities will require using specific timezones. The command will highlight when it is unable to match - for example, the prompt `4pm` `Fort Worth` returns:

`• ‼️ No match: Fort Worth`

In this case, the better prompt would be `4pm` `US Central`.

## Setup Notes
Requires python 3.10+ which includes `ZoneInfo` and the match case statement. It also should have `pip3` installed by default, which is needed to install two supporting packages (see below).

There are three (easy) things that you'll need to do when you first use this command.
1. The first time you run this, you will be prompted to allow Raycast to access `System Events`, which is required in order for the command to paste the results.

	This script requires two additional python packages, both of which require that you use the Terminal (Terminal.app, which comes with macOS): 

2. Install `[dateparser](https://dateparser.readthedocs.io/en/latest/)` via the command line:

 	`pip3 install dateparser`

3. Install `applescript` via the command line:

	`pip3 install applescript`

## Configuration
In the "CONFIGURATION" section of time-converter.py, there are three options you can modify:

#### default_locations
The locations listed here will be used if nothing is specified, which is handy if you routinely use this for a specific location or set of locations. This list is initially set to `Austin, London, Sofia`

#### default_format 
This script outputs the processed times on a single line by default ("inline"). You can change it to `list` if you want it to output a bulleted list by default. You can override either setting as needed when you invoke the Raycast command.
 
#### include_parsed_time_zone
This is set to `False` by default, which provides cleaner output, but you can set it to `True` to have the script include the parsed timezone in the output. This can help you validate that the right timezone was selected. It will appear like:

`4:00 PM - NYC (US/Eastern) • 9:00 PM - London (UTC) • 2:30 AM - Kolkata (Asia/Kolkata)`

### Special Cases
There is a section in the script that maps common cities, acronyms (NYC for New York City, ATX for Austin, Texas) or regions to specific timezones. You can add more if you're comfortable.

See the file `timezone_list.csv` to see the full list of available timezones (made available by your system and surfaced through the `[zoneinfo](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo)`).

## To-Do
- Determiene how to disable copy-to-clipboard as it now pastes directly


### Credits & Acknowledgements
Inspired by the [Timezone Expander Alfred workflow](https://github.com/devonzuegel/timezone-expander.alfredworkflow) by [Devon Zuegel](https://devonzuegel.com)