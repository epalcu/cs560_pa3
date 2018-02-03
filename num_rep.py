import sys
import os
import re
import time

titles = {}
links = {}

def open_file(lines):
    with open("adj_list.txt") as fname:
        lines = fname.readlines()
    fname.close()
    return lines

def write_to_dicts(line):
    global val
    title, link = line.split('\t')
    t = title.rstrip()
    l = link.rstrip()

    # Add all titles to titles dictionary with their corresponding numerical value
    # If title in links dictionary, simply add it with its value to the titles dictionary
    if (t in links.keys()):
        titles[t] = links[t]
    elif (t not in titles.keys()):
        try:
            titles[t] = val
            val += 1
        except:
            val = 0
            titles[t] = val
            val += 1

    # Add all links to links dictionary with their corresponding numerical value
    # If link in titles dictionary, simply add it with its value to the links dictionary
    if (l in titles.keys()):
        links[l] = titles[l]
    elif (l not in links.keys()):
        try:
            links[l] = val
            val += 1
        except:
            val = 0
            links[l] = val
            val += 1

    # Write to file the numerical representation of the titles and links
    open("num_rep.txt", "a").write("{0}\t{1}\n".format(titles[t], links[l]))

def print_titles(dict):
    open("titles.txt", "w").write("\n")
    for key, value in dict.items():
        #print "{0} --> {1}".format(key, value)
        open("titles.txt", "a").write("{0} --> {1}\n".format(key, value))

def print_links(dict):
    open("links.txt", "w").write("\n")
    for key, value in dict.items():
        #print "{0} --> {1}".format(key, value)
        open("links.txt", "a").write("{0} --> {1}\n".format(key, value))

if __name__ == "__main__":
    lines = []

    # Open file and read lines into list
    lines = open_file(lines)

    # Initialize file for writing to
    open("num_rep.txt", "w").write("\n")

    # Write Titles and Links to the respective dictionaries
    map(write_to_dicts, lines)

    #print_titles(titles)
    #print_links(links)
