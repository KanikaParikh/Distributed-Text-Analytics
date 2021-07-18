#!/usr/bin/python

# Kanika Parikh 216030215 and Kaumilkumar Patel 216008914
# Assignment 2 : Part C

import sys
import re
import csv 

checkin_csv = csv.reader(sys.stdin)
# to skip the First Row
next(checkin_csv) 

for row in checkin_csv:
    # Business_id
	bus_id = row[0]

    # Extract category column
	categories = row[12].split(';') 

	for i in categories:
        # Print the categories elements and business_id separated with tab.
		print(i + '\t' +  bus_id)
	