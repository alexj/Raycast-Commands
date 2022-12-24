#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Time Converter
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName Time Converter
# @raycast.argument1 { "type": "text", "placeholder": "Time" }
# @raycast.argument2 { "type": "text", "placeholder": "Location(s)" }

# Documentation:
# @raycast.description Takes a time and outputs the time in one or more timezones
# @raycast.author Alex Jones

# print(sys.version)

import sys
from datetime import datetime
import zoneinfo
from zoneinfo import ZoneInfo
import dateparser
import difflib

# ----- Caching (DISABLED) ----
# Cache the list of timezones - unused as no clear benefit to execution time
# See https://adamj.eu/tech/2021/05/06/how-to-list-all-timezones-in-python/?

# from functools import lru_cache

# @lru_cache(maxsize=None)
# def get_timezones():
#     return zoneinfo.available_timezones()
# tz_list = get_timezones() # used if we want to cache
# ------------------------------

time_format = "%-I:%M%p"
source_time = sys.argv[1]
source_locations = sys.argv[2]
timezones = [location.strip() for location in source_locations.split(",")]
tz_list = zoneinfo.available_timezones()
parsed_date = dateparser.parse(source_time)

print( "Input Time: " + source_time + " - Parsed: " + str(parsed_date) + " (" + dateparser.parse(source_time).strftime(time_format) + ")" )

print(timezones)
print ("\n")

for zone in timezones:
	zone_input = zone
	match zone:
		case "LA" | "la":
			zone = "America/Los_Angeles"
			zone_input = "Los Angeles"
			zone_input = zone_input + "*" # highlight specified timezones
		case "NY" | "ny":
			zone = "America/New_York"
			zone_input = "New York"
			zone_input = zone_input + "*"
		case _:
			zone = difflib.get_close_matches(zone.title(),tz_list,cutoff=.35)[0]
	time_in_new_timezone = parsed_date.astimezone(ZoneInfo(zone))
	print(zone_input.title() + " (" + zone + "): " + time_in_new_timezone.strftime(time_format))
	
	
	
	