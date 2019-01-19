# sample code to fetch a list of restaurants using zomatopy

import pprint, json
import zomatopy

# specify location and cuisine
loc = 'Bengaluru'
cuisine = 'Italian'

# provide API key and initialise a 'zomato app' object
config={ "user_key": "08097ba0652c0ac066a2a45d5affb9e1"}
zomato = zomatopy.initialize_app(config)

# get_location gets the lat-long coordinates of 'loc'
location_detail=zomato.get_location(loc, 1)

# store retrieved data as a dict
d1 = json.loads(location_detail)

# separate lat-long coordinates
lat=d1["location_suggestions"][0]["latitude"]
lon=d1["location_suggestions"][0]["longitude"]

# cuisines code (used by zomatopy)
cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
#mcuisines = str(cuisines_dict.get(cuisine))
#print(type(mcuisines), 'mcusisines = ', mcuisines)
city_ID = zomato.get_city_ID(loc)
cuisines = zomato.get_cuisines(city_ID)
cuisine_id = str(list(cuisines.keys())[list(cuisines.values()).index(cuisine)])

# fetch and print results
results=zomato.restaurant_search("",latitude=lat, longitude=lon, cuisines=cuisine_id, limit=1)
d = json.loads(results)
res_name = d['restaurants'][0]['restaurant']['name']
res_loc = d['restaurants'][0]['restaurant']['location']['address']
print('\n', 'Restaurant: ', res_name, res_loc, '\n')
#pprint.pprint(d)