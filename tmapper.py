#!/usr/bin/python

# Kanika Parikh 216030215 and Kaumilkumar Patel 216008914
# Assignment 2 : Part A

import csv
import re
import sys

for row in sys.stdin:

    # Strips the input - eliminates the trailing spaces in beginning and end
    row = row.strip()

    # Splits the csv file in columns
    column = row.split(',')

    # Only take first column from yelp_tip.csv 
    # \W means anything that isn't word a-zA-Z0-9, ^ start of string $ end of sting + one or more
	# Remove anything that is not word char or number: i.e special character space, punctation comma etc
    line = re.sub(r'^\W+|\W+$', '', column[0]) 
    
    # Next is to remove special chars from words in a line : split the word at special character 
    words = re.split(r'\W+', line)


    for w in range(len(words)-2):
        # \t tab char to separate key value pair.    
        print(words[w] + " "+ words[w+1] + " "+ words[w+2]+ "\t" + "1")