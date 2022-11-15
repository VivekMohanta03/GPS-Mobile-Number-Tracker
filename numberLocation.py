import imp
import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

Key = 'f3196499edb149e9bc0286cd024fa654'
sanNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(sanNumber, "en")
print(yourLocation)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = yourLocation).add_to(myMap)
# save map in html file
myMap.save("MyLocation.html")