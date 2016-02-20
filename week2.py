import re

data = open("regex_sum_219862.txt")

sum = 0

for line in data:
	line = line.rstrip()

	y = re.findall("[0-9]+",line)

	for info in y:
		sum = sum + int(info)

print sum