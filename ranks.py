import sys
import os
import re
import time
import operator

nums = {}

# Read in file of summed links per title
with open("hadoop_results.txt") as fname:
    lines = fname.readlines()
    for line in lines:
        title, num_links = line.split('\t')
        t = title.rstrip()
        nl = float(num_links.rstrip())

        if (nl in nums.keys()):
            nums[nl].append(t)
        else:
            nums[nl] = [t]
fname.close()

# Sort the titles to establish ranks
sorted_nums = sorted(nums.items(), key=operator.itemgetter(0))
# Reverse list so titles with largest number of links to be first
sorted_nums = list(reversed(sorted_nums))

# Print out the ranks and titles
rank = 1
for i in sorted_nums:
    for title in i[1]:
        print "Rank {0}: {1}".format(rank, title)
    rank += 1
