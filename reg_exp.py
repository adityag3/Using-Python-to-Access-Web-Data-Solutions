#This header file contains regular expression which makes extraction of a desired strings from a collection easy
import re

#Opening a text file with sample code
cool = open("reg_exp.txt")

#This is use of just one regular expression
'''
for line in cool:
	line = line.rstrip()
	if re.search(":",line):
		print 'a ->' + line
	if re.search("^:",line):
		print 'b ->' + line
	if re.search(":$",line):
		print 'c ->' + line
'''

#This is use of combination of regular expressions
'''
for line in cool:
	line = line.rstrip()

	if re.search("^X.*:$",line):
		print "a ->" + line

	if re.search("^X\S+:.*:$",line):
		print "b ->" + line
'''

#This makes use of square brackets for string

"""

for line in cool:
# y is collection of digit values in th line
	y = re.findall("[0-8]+",line)
	print y	

"""

y = "Xmas sucks"
for x in y:
	print "Merry"