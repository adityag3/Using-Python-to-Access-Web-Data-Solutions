import re, urllib
from bs4 import BeautifulSoup

url = raw_input("Enter URL: ")

count = raw_input("Enter count: ")

pos = raw_input("Enter position: ")

for x in range(0,int(count)+1):

	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	head = soup("h1")
	tags = soup("a")

	tag = tags[int(pos)-1]
	head = str(head)
	name = re.findall("People that (\S+)",head)

	url = tag.get("href",None)

	print "Retrieving: " + str(url)

print name[-1]

