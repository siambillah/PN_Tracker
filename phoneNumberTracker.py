from phonenumbers import *
from folium import *
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder, carrier

number = input("Type your Number with Country code: ") #'+8801722668241'

#get mobile number location I mean country name
ch_number = parse(number, "CH")
location = geocoder.description_for_number(ch_number, "en")
print("Your Number      : " + number)
print("Country          : " + location)

# get service provider Name 
service_number = parse(number, "RO")
sp_name = carrier.name_for_number(service_number, "en")
print("Service Provider : " + sp_name)

# Opencagedata Site Location Tracker API
key = 'b6d56fca32144409b13265b859a62027'

# here is the Opencage coding
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

# geting latitude and langitude
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print("Here is your location: ", lat, lng)

#get your locatopn as map
myMap = Map(location=[lat, lng], zoom_start=9)
Marker([lat, lng], popup=location).add_to(myMap)

# get your Location save as html file
myMap.save(number + " location.html")
print("Save the location map in html file, Open it in browser")
