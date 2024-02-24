#!/usr/bin/env python3

import sys
import re
import operator
import csv

error = {}
per_user = {}

f = open("syslog.log", "r")
'''Searching Data in Log and store in Dict'''
for log in f:
   result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", log)
   if result.group(2) not in error.keys():
     error[result.group(2)] = 0
   error[result.group(2)] += 1
   if result.group(3) not in per_user.keys():
      per_user[result.group(3)] = {}
      per_user[result.group(3)]["INFO"] = 0
      per_user[result.group(3)]["ERROR"] = 0


   if result.group(1) == "INFO":
      per_user[result.group(3)]["INFO"] += 1
   else:
      per_user[result.group(3)]["ERROR"] += 1

'''Sorted Dict'''
error = sorted(error.items(), key = operator.itemgetter(1), reverse = True)
per_user = sorted(per_user.items())

f.close()
error.insert(0, ("Error", "Count"))

'''Write in Csv file '''
f = open("user_statistics.csv", "w")
f.write("Username, INFO, ERROR\n")
for user in  per_user:
   a, b = user
   f.write(str(a) + "," + str(b["INFO"]) + "," + str(b["ERROR"]) + "\n")
f.close()

f = open("error_message.csv", "w")
for err in error:
   a, b = err
   f.write(str(a) + "," + str(b) + "\n")
f.close()