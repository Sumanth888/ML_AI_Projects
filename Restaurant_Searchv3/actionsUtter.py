from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.actions.forms import FormAction
from rasa_core.actions.forms import EntityFormField, BooleanFormField


import json

import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

class ActionSetSlotValues(FormAction):

	def name(self):
		return 'action_set_slot'
	
	@staticmethod
	def required_fields():
		return [
			EntityFormField("location", "location"),
            EntityFormField("cuisine", "cuisine"),
            EntityFormField("budget", "budget")
        ]
	
	def slot_mappings(self):
		return {"location": self.from_entity(entity="location", intent="None"),
				"cuisine": self.from_entity(entity="cuisine",intent="None"),
				"budget": self.from_entity(entity="budget",intent="None")}
				
	
	def submit(self, dispatcher, tracker, domain):
		return []


class ActionValSlotValues(Action):

	def name(self):
		return 'action_val_slot'
	
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		email = tracker.get_slot('emailid')
		if cuisine is not None:
			cuisine_list=['chinese','mexican','italian','american','south indian','north indian']
			if cuisine.lower() not in cuisine_list:
				dispatcher.utter_template('utter_wrong_cuisine', tracker)
				SlotSet('cuisine', None)
				
		if loc is not None:
			folder = Path('./data')
			loc_df = pd.read_csv(folder/'city.txt', encoding = "utf-8")
			if loc_df.size > 0 :
				city_list=[x.lower() for x in loc_df['City'].values.tolist()]
				if str(loc.values).lower() not in city_list:
					dispatcher.utter_template("utter_wrong_location",tracker)
					SlotSet('location', None)
					
		if budget is not None:
			budget_list=['More than 700','Rs. 300 to 700','Lesser than Rs. 300']
			if budget not in budget_list:
				dispatcher.utter_template('utter_wrong_budget', tracker)
				SlotSet('budget', None)
				
		if email is not None:
			pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
			if not re.match(pattern, email.lower()):
				dispatcher.utter_template("utter_wrong_emaildid",tracker)
				SlotSet('emailid', None)
					
		return []

class ActionUtterAndSetSlotEml(Action):

	def name(self):
		return 'action_set_slotEml'
		
	def run(self, dispatcher, tracker, domain):
			setval = tracker.get_slot("emailid")
			if (setval !=''):
				your_slot_value = setval
			else:
				your_slot_value = tracker.latest_message.text
			
			pattern = "[a-zA-z0-9]+(\.)?[a-zA-z0-9]*(@)[a-zA-z0-9]+(\.com)$"
			if not re.match(pattern, your_slot_value):
				dispatcher.utter_template("utter_wrong_emaildid",tracker)
			else:
				return [SlotSet('emailid',your_slot_value)]				
				