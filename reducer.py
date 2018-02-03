#!/usr/bin/python
import sys
import os
import re
import time
import copy
import operator

titles = {}

class Reducer():
    def readin_pairs(self):
        for input in sys.stdin:
            title, rank, link = input.split('\t', 2)
            t = title.rstrip()
            r = rank.rstrip()
            l = link.rstrip()
            self.add_to_dict(t, float(r), l)

    def add_to_dict(self, t, r, l):
            # Create dictionary of all titles with their incoming links as values
            if (t in titles.keys()):
                # Make sure links don't point to themselves
                if (l != t):
                    num = titles[t]['num_links']
                    titles[t]['num_links'] = num + r
                    titles[t]['links'].append((l, 0.0))
                # Remove duplicates within list of links for each title key
                links = titles[t]['links']
                titles[t]['links'] = list(set(links))
            else:
                # Make sure links don't point to themselves
                if (l != t):
                    titles[t] = {'num_links': r, 'links': [(l, 0.0)]}
                else:
                    titles[t] = {'num_links': 0.0, 'links': []}

    def sum_links(self):
        # Make copy of current titles dictionary to later establish at what iteration convergence is achieved
        prev_titles = copy.deepcopy(titles)
        # Perform 25 iterations to calculate page ranks
        for iter in range(25):
            #sys.stderr.write("{0}\n".format(iter))
            # Traverse across keys within titles dictionary
            for key in titles.keys():
                # Retrieve number of links for current key
                title_links = titles[key]['num_links']
                # Traverse tuples within list of links for current key
                for i in range(0, len(titles[key]['links'])):
                    link = titles[key]['links'][i][0]
                    num = titles[key]['links'][i][1]
                    # If the link exists as a key in the titles dictionary
                    if (link in titles.keys()):
                        # Pull out its number of links
                        num_links = titles[link]['num_links']
                        # Set the link's number of links to the value
                        titles[key]['links'][i] = (link, num_links)
                        # Calculate the number of extra links found since last iteration
                        new_links = num_links - num
                        # Now add it to the total number of links for current key
                        titles[key]['num_links'] = title_links + new_links

            # Test to see if convergence achieved before 25 iterations; otherwise, set prev_titles dictionary to current titles dictionary
            # if (titles == prev_titles):
            #     sys.stderr.write("Convergence achieved at iteration {0}.\n".format(iter))
            # else:
            #     prev_titles = copy.deepcopy(titles)

    def print_sums(self):
        for key in titles.keys():
            print '%s\t%s' % (key, titles[key]['num_links'])

    def write_dict(self):
        open("r.txt", 'w').write('\n')
        for key, value in titles.items():
            open("r.txt", 'a').write("{0} --> {1}\n".format(key, value))

if __name__ == "__main__":
    reducer = Reducer()
    start = time.time()

    reducer.readin_pairs()
    reducer.sum_links()

    stop = time.time() - start

    reducer.print_sums()
    #reducer.write_dict()

    sys.stderr.write("Total elapsed time: {0} secs.\n".format(stop))
