import phonenumbers
import opencage
from phonenumbers import geocoder
number="+31633481806"
pepnumber= phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode
key="d5583258021c4372bebea259f271c33a"
geocoder = OpenCageGeocode(key)
query= str(location)
result=geocoder.geocode(query)
print(result)
lat =result[0]['geometry']['lat']
lng= result[0]['geometry']['lng']
print(lat,lng)