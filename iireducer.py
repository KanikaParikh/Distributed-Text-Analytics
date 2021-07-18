#!/usr/bin/python

# Kanika Parikh 216030215 and Kaumilkumar Patel 216008914
# Assignment 2 : Part C

import re
import sys

previous = None
count = 0

var='' # empty string

# For evry line we read, if the word appears for first time then  
for line in sys.stdin:

    # split key and value line by line at tab.
    key,value = line.split('\t')

    if key != previous: # New Key
        if previous is not None: # Key is found for first time.
            
            var = var.replace("\n","") # removes new line character
            
            print('\n') # prints the new index on a new line.
            # print the business id on sameline.
            print(str(previous) + ":" + str(var[:-2]) , end='')

        previous = key # assign new key to previous with count as 0
        var = '' # empty for new key
    var = str((var + value + ', ')) # appending the key with new values

# for last value in csv file
print('\n')
var = var.replace("\n","") # removes new line character
print(str(previous) + ":" + str(var[:-2]) , end='') # print the value for previous key