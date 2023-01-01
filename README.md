# Raycast Commands

## Time-Converter
This command takes a time (local to your machine) as the first input and one or more comma-separated locations as the second input, and then returns the time in the specified locations.

For example (typed in US Central Timezone):

`3PM` `NYC, London, Kolkata`

returns

```
• 4:00 PM - NYC (US/Eastern)

• 9:00 PM - London (UTC)

• 2:30 AM - Kolkata (Asia/Kolkata)
```

The command understands both 24-hour and 12-hour notation (the latter AM/PM or am/pm), with or without minutes as well as "fuzzy" times, such as "now" or "4PM tomorrow".

*Note:* the command does it's best to match input to timezones and most world capitals and major cities show up, but many cities will require using specific timezones. The command will highlight when it is unable to match - for example, the prompt `4pm` `Fort Worth` returns:

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