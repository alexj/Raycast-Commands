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
from zoneinfo import ZoneInfo
import dateparser

timezones = ['America/Los_Angeles', 'Europe/Madrid', 'America/Puerto_Rico', 'Australia/Brisbane' ]
print(timezones)
time_format = "%-I:%M%p"
source_time = sys.argv[1]
source_locations = sys.argv[2]
print(source_locations.split(","))
# timezones = source_locations.split(",")
timezones = [location.strip() for location in source_locations.split(",")]
print(timezones)
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

# server_timezone = "US/Eastern"
# new_timezone = "US/Pacific"
# current_time = datetime.now(ZoneInfo(server_timezone)) 
# time_format = "%Y-%m-%d %H:%M:%S"

# current_time_in_new_timezone = ???
# current_time_in_new_timezone = current_time.astimezone(ZoneInfo(new_timezone))

# print("Current time: " + current_time.isoformat(timespec='seconds'))
# 2021-10-04T02:42:54-04:00

# print(repr(current_time))
# datetime.datetime(2021, 10, 4, 2, 42, 54, 40600, tzinfo=zoneinfo.ZoneInfo(key='US/Eastern'))

# print(current_time_in_new_timezone.isoformat(timespec='seconds'))
# 2021-10-03T23:42:54-07:00

# print(repr(current_time_in_new_timezone))
# datetime.datetime(2021, 10, 3, 23, 42, 54, 40600, tzinfo=zoneinfo.ZoneInfo(key='US/Pacific'))

#print("Hello World! Argument1 value: " + sys.argv[1])
# print( dateparser.parse('12/12/12') )

print( "DateParser (" + source_time + "): " + dateparser.parse(source_time).strftime(time_format) )
parsed_date = dateparser.parse(source_time)
print(parsed_date)
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
for zone in timezones:
	time_in_new_timezone = parsed_date.astimezone(ZoneInfo(zone))
	print(zone + ": " + time_in_new_timezone.strftime(time_format))