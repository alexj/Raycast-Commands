#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Time Converter
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🕔
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
# def get_time_zones():
#     return zoneinfo.available_timezones()
# tz_list = get_time_zones() # used if we want to cache
# ------------------------------

time_format = "%-I:%M %p"
source_time = sys.argv[1]
source_locations = sys.argv[2]
time_zones = [location.strip() for location in source_locations.split(",")]
tz_list = zoneinfo.available_timezones()
parsed_date = dateparser.parse(source_time)

print( "Input Time: " + source_time + " - Parsed: " + str(parsed_date) + " (" + dateparser.parse(source_time).strftime(time_format) + ")" )

print(time_zones)
print ("\n")

for zone in time_zones:
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
		print(time_in_new_time_zone.strftime(time_format) + " - " + zone_input + " (" + zone + ")" )
	else:
		print("‼️ No match: " + zone_input)
