from phonenumbers import *
from folium import *
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder, carrier

number = input("Type your Number with Country code: ") #'+8801722668241'

ch_number = parse(number, "CH")
location = geocoder.description_for_number(ch_number, "en")
print("Your Number      : " + number)
print("Country          : " + location)

service_number = parse(number, "RO")
sp_name = carrier.name_for_number(service_number, "en")
print("Service Provider : " + sp_name)

key = 'b6d56fca32144409b13265b859a62027'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
# list1 = results[0]
# print(list1)
# list2 = results[1]
print(lat, lng)
for i in results:
    print(i)

# myMap = Map(location=[lat, lng], zoom_start=9)
# Marker([lat, lng], popup=location).add_to(myMap)

# myMap.save(number + " location.html")
# print("Save the location map in html file, Open it in browser")


