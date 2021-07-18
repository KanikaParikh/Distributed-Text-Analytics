#!/usr/bin/python

# Kanika Parikh 216030215 and Kaumilkumar Patel 216008914
# Assignment 2 : Part B

import sys
import re


# --------- Helper Function to sort days -----------
def sorter_print(l):

    priority = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    dic = {}
    for line in l:
        k = re.split(",", line)[1]
        dic[priority.index(k)] = line
    
    dictionary_items = dic.items()
    sorted_items = sorted(dictionary_items)
    for t in sorted_items:
        print(t[1])
    
    

firstline = sys.stdin.readline()
key, value = re.split("\t",firstline)
pk1, pk2 = re.split(" ", key) # splitting bus_id and day
count = int(value) # checkin values

list_to_print = [] # To store list of bus_id with unsorted days


for line in sys.stdin:
    key, value = re.split("\t",line)
    k1, k2 = re.split(" ", key)
    
    # if next key is same to previous bus_id then check for values of day and add the checkins
    # otherwise print the list of bus_id with sorted days
    if k1 == pk1:

        if k2 == pk2:
            count += int(value)
        else:
            
            list_to_print.append(k1 + "," + pk2 + "," + str(count))
            count = int(value)
            pk2 = k2
    else:
        list_to_print.append(pk1 + "," + pk2 + "," + str(count))

        pk1 = k1
        pk2 = k2

        count = int(value)
        sorter_print(list_to_print)
        list_to_print = []

list_to_print.append(pk1 + "," + pk2 + "," + str(count))
sorter_print(list_to_print)