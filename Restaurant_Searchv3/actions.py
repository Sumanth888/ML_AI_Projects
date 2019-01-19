from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from collections import OrderedDict
import zomatopy
import json


class ActionSearchRestaurants(Action):
	
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"7657af8025bf771012673de9bf8b16cb"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		low=0
		high=999999
		if budget =="Lesser than Rs. 300" :
			low = 0
			high=300
		elif budget =="Rs. 300 to 700" :
			low=300
			high=700
		elif budget =="More than 700":
			low=700
			high=999999
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':10,'mexican':15,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		cnt=1
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				if (restaurant['restaurant']['average_cost_for_two']>=low) & (restaurant['restaurant']['average_cost_for_two']<=high) :
					cnt = cnt + 1
					if cnt > 5 :
						break
					else:
						response=response+ " "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+".\n"
		if response=="":
			dispatcher.utter_message("Sorry no results found for the criteria")
			dispatcher.utter_template("utter_goodbye", tracker)
		else:
			dispatcher.utter_message("-----"+response)
		return []
