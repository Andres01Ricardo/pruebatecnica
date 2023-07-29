import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCxReuuM3CkAV5vLinf5FlLbD8hqwLTrIY')

def geocoding(address):
  geocode_result = gmaps.geocode(address)
  lat=geocode_result[0]['geometry']['location']['lat']
  lng=geocode_result[0]['geometry']['location']['lng']
  return lat,lng

def neighborhood(lat, lng):
  reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
  for i in range(4):
    if(reverse_geocode_result[0]['address_components'][i]['types'][0] == 'neighborhood'):
      neighborhood=reverse_geocode_result[0]['address_components'][i]['long_name']
  return neighborhood

def recursiveneighborhood(neighborhoodresultprevious,numberAddress):
  neighborhoodresult = neighborhoodresultprevious
  while neighborhoodresult == neighborhoodresultprevious:
    numberAddress+=100
    addressfinal=str(numberAddress) + ' SE Stark Streett, Portland, OR 97214'
    lat,lng = geocoding(addressfinal)
    neighborhoodresult = neighborhood(lat, lng)
  return neighborhoodresult,addressfinal

numberAddress=1300

lat,lng = geocoding(str(numberAddress) + ' SE Stark Streett, Portland, OR 97214')
print('lat:', lat,' - lng:',lng)

neighborhoodresult = neighborhood(lat, lng)
print('neighborhood: ',neighborhoodresult)

neighborhoodresultchange,addressfinal = recursiveneighborhood(neighborhoodresult,numberAddress)
print('neighborhood: ',neighborhoodresultchange, ' - final address: ',addressfinal)
