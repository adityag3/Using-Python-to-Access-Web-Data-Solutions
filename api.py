import urllib   #This header file allows us to access websites data.
import json     #Inbuilt python library to access and manipulate json type data.

#Google geolocator api url link.
service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
	#Address can be explicit or just a landmark. It can also have spelling errors.
	address = raw_input("Enter Address: ")

	if len(address) < 1:
		break

	#Using Json data we create a url for Google Geolocator API.
	url = service_url + urllib.urlencode({ 'sensor' : 'false' , 'address' : address })

	print 'Retriving', url

	uh = urllib.urlopen(url)

	data = uh.read()

#	print "Total " , len(data) , " found."

	try: js = json.loads(str(data))

	except: js = None

	if 'status' not in js or js['status'] != 'OK':
		print "-----Failed to retrieve information-----"
		print data
		continue


#	print json.dump(js,indent = 4)

	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lat"]
	location = js["results"][0]["formatted_address"]

	print "Latitude:  ", lat
	print "Longitude: ", lng
	print "Location:  ", location


