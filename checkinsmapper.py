#!/usr/bin/python

# Kanika Parikh 216030215 and Kaumilkumar Patel 216008914
# Assignment 2 : Part B

import sys
import csv

checkin_csv = csv.reader(sys.stdin)
# to skip the First Row
next(checkin_csv) 

for row in checkin_csv:

    bus_id= row[0]
    days= row[1]
    checkins = row[3]
    print(bus_id + " " + days + "\t" + checkins )
    
    