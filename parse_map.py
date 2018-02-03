import xml.etree.ElementTree as ET
import time
import sys
import re

# Parse XML and create tree from it
tree = ET.parse('simplewiki-20161120-pages-articles-multistream.xml')
root = tree.getroot()

# Open file of all valid Wiki titles, and read lines
tf = open('simplewiki-20161120-all-titles')
tf.readline()

validTitles = []

# For each line from file, append only the valid title to a list
for line in tf:
	w1, w2 = line.split('\t')
	w2 = w2.rstrip()
	validTitles.append(w2);

# Establish the working namesapce
namespace = '{http://www.mediawiki.org/xml/export-0.10/}'

contents = []

# Create a set of the valid titles list to remove duplicates and improve lookup time
vt = set(validTitles)

# Function called by map to do link comparisons
def find_valids(link):
	if link in vt:
		open("links_map.txt", "a").write("{0}\t{1}\n".format(article, link))

# Create file to append to later
open("links_map.txt", "w").write("\n")
global article
begin = time.time()

# Traverse each page within XML tree
for page in root.findall(namespace+'page'):
	title = page.find(namespace+'title')
	article = title.text
	revision = page.find(namespace+'revision')
	text = revision.find(namespace+'text')
	start = "\[\["
	end = "\]\]"
	try:
		# Find all links, indicated by the "[[ ]]" notation, and create list from them
		links = re.findall('%s(.*)%s' % (start, end), text.text, flags = re.MULTILINE)

		# Iterate across links list with map
		map(find_valids, links)
	except:
		continue

finish = time.time() - begin
print("Total elapsed computational time: {0}".format(round(finish, 2)))

exit()
