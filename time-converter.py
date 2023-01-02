#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Time Converter
# @raycast.mode silent 

# Optional parameters:
# @raycast.icon 🕔
# @raycast.packageName Time Converter
# @raycast.argument1 { "type": "text", "placeholder": "Time" }
# @raycast.argument2 { "type": "text", "placeholder": "Location(s)", "optional": true }
# @raycast.argument3 { "type": "text", "placeholder": "Format (list or inline)", "optional": true }

# Documentation:
# @raycast.description Takes a time and outputs the time in one or more timezones
# @raycast.author Alex Jones

import sys
from datetime import datetime
import zoneinfo
from zoneinfo import ZoneInfo
import dateparser
import difflib
import subprocess
import applescript

# print(sys.version)

# ----- Caching (DISABLED) ----
# Cache the list of timezones - unused as no clear benefit to execution time
# See https://adamj.eu/tech/2021/05/06/how-to-list-all-timezones-in-python/?

# from functools import lru_cache

# @lru_cache(maxsize=None)
# def get_time_zones():
#     return zoneinfo.available_timezones()
# tz_list = get_time_zones() # used if we want to cache
# ------------------------------


# ========== CONFIGURATION ==========

default_locations = "Austin, London, Sofia"  #These locations will be used if nothing is specified
default_format = "inline"  # Can be "list" for a bulleted list or "inline" for inline results 
include_parsed_time_zone = False  # When set to True, the parsed timezone will be included in the output, which can help you validate the right timezone waa selected

# ========== END CONFIGURATION ==========

time_format = "%-I:%M %p"
time_zone_output = ''
source_time = sys.argv[1]
source_locations = sys.argv[2]
if not source_locations:
	source_locations = default_locations
time_zones = [location.strip() for location in source_locations.split(",")]
tz_list = zoneinfo.available_timezones()
parsed_date = dateparser.parse(source_time)
output_format = sys.argv[3] # 'l' for list or 'i' for inline
if not output_format:
	output_format = default_format
parsed_zone_output = ''

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

for index, zone in enumerate(time_zones):
	zone_input = zone
	match = 1
	match zone:
		case "Atlanta" | "atlanta" | "ATL" | "atl" | "Boston" | "boston" | "EDT" | "edt" | "EST" | "est" | "Miami" | "miami" | "NY" | "ny" | "NYC" | "nyc":
			zone = "US/Eastern"
		case "Austin" | "austin" | "ATX" | "atx" | "CDT" | "cdt" | "CST" | "cst" | "Dallas" | "dallas" | "Houston" | "houston" | "San Antonio" | "san antonio":
			zone = "US/Central"
		case "Boulder" | "boulder" | "Denver" | "denver" | "El Paso" | "el paso" | "MDT" | "mdt" | "MST" | "mst":
			zone = "US/Mountain"
		case "LA" | "la" | "Portland" | "portland" | "PDT" | "pdt" | "PST" | "pst"| "San Diego" | "san diego" | "San Francisco" | "san francisco" | "SF" | "sf":
			zone = "US/Pacific"
		case "Cape town" | "cape town" | "Capetown" | "capetown":
			zone = "Africa/Johannesburg"
		case "England" | "england" | "GB" | "gb" | "London" | "london" | "UK" | "uk":
			zone = "UTC"
		case "New Zealand" | "new zealand" | "NZ" | "nz":
			zone = "Pacific/Auckland"
		case "sofia" | "Sofia":
			zone ="Europe/Sofia"
		case _:
			try:
				zone = difflib.get_close_matches(zone,tz_list,cutoff=.6)[0]
#				zone = difflib.get_close_matches(zone.title(),tz_list,cutoff=.35)[0] # Title case helps for some inputs, but ruins acronyms like CDT
			except:
				match = 0
				zone = "UTC"
	if match == 1:
		time_in_new_time_zone = parsed_date.astimezone(ZoneInfo(zone))
		
		if include_parsed_time_zone == True:
			parsed_zone_output = " (" + zone + ")"
			
		if (output_format == 'l' or output_format == 'list'):
			time_zone_output += "• " + time_in_new_time_zone.strftime(time_format) + " - " + zone_input + parsed_zone_output + "\n"
		else:
			time_zone_output += time_in_new_time_zone.strftime(time_format) + " " + zone_input + parsed_zone_output
			if index == len(time_zones) - 1:
				print ('')
			else:
				time_zone_output += " / "
	else:
		if (output_format == 'l' or output_format == 'list'):
			time_zone_output += "• ‼️ No match: " + zone_input + "\n"
		else:
			time_zone_output += "‼️ No match: " + zone_input + " • "
print(time_zone_output)
try:
	write_to_clipboard(time_zone_output)

	resp = applescript.tell.app("System Events",'''
	tell application "System Events"
	  tell process 1 where frontmost is true
	    click menu item "Paste" of menu "Edit" of menu bar 1
	  end tell
	end tell
	''')
	assert resp.code == 0, resp.err
except:
 	print("😕 Sorry, something went wrong when outputting the results.")