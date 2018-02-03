#!/usr/bin/python
import sys
import os
import re
import time

class Mapper():
    def readin_pairs(self):
        for input in sys.stdin:
            title, link = input.split('\t')
            t = title.rstrip()
            l = link.rstrip()

            # Print out title, initial rank (1.0), and its in-link
            print '%s\t%s\t%s' % (t, 1.0, l)

if __name__ == "__main__":
    mapper = Mapper()
    mapper.readin_pairs()
