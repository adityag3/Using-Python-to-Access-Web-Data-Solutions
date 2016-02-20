import json
import urllib

url = raw_input("Enter URL: ")

uh = urllib.urlopen(url)

data = uh.read()

try: js = json.loads(str(data))

except: js = None

values = js["comments"]

sum = 0

for value in values:
	sum = sum + int(value["count"])

print sum
