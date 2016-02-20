import re, urllib  #regular expression and urllib libraries are imported
from bs4 import BeautifulSoup as BS #We will use BS in place of Beautifulsoup in the whole program
import xml.etree.ElementTree as ET

url = raw_input("Location: ")

xml_data = urllib.urlopen(url).read()

xml_data = str(xml_data)

tree = ET.fromstring(xml_data)

values = tree.findall('comments/comment')

sum = 0

for value in values:
	value = value.find('count').text
	sum = sum + int(value)

print sum