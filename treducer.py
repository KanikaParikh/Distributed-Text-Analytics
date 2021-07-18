#!/usr/bin/python

# Kanika Parikh 216030215 and Kaumilkumar Patel 216008914
# Assignment 2 : Part A

import re
import sys

previous = None
count = 0
#with open('output.txt', 'r') as file:

# For evry line we read, if the word appears for first time then  
for line in sys.stdin:

    # split key and value line by line at tab.
    key,value = re.split('\t', line)

    #key = line[0]
    if key != previous: # New Key
        if previous is not None: # Key is found for first time.
            print(str(previous) + "\t" + str(count)) # print the value for previous key
        previous = key # assign new key to previous with count as 0
        count = 0

    # if value is same as above, keep on increasing the counter
    count = count + int(value)
print(str(previous) + "\t" + str(count))   
