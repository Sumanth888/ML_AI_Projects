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
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
			EntityFormField("location", "location"),
            EntityFormField("cuisine", "cuisine"),
            EntityFormField("budget", "budget"),
        ]
		
    def name(self):
        return 'action_set_slot'

    def submit(self, dispatcher, tracker, domain):
        return []


class ActionUtterAndSetSlotLoc(Action):
	def name(self):
		return 'action_set_slotLoc'
		
	def run(self, dispatcher, tracker, domain):
		folder = Path('./data')
		setval = tracker.get_slot("location")
		if (setval !=''):
			your_slot_value = setval
			your_slot_value = your_slot_value[0]		
		else:
			your_slot_value = tracker.latest_message.text
		
		print('tracker.latest_message.text =' , tracker.latest_message.text)
		print('your_slot_value =', your_slot_value)
		
		loc_df = pd.read_csv(folder/'city.txt', encoding = "utf-8")
		if loc_df.size > 0 :
			city_list=[x.lower() for x in loc_df['City'].values.tolist()]
			if (your_slot_value == None):
				dispatcher.utter_template("utter_wrong_location",tracker)
			elif (your_slot_value.lower() not in city_list):
				dispatcher.utter_template("utter_wrong_location",tracker)				
			else:
				return [SlotSet('location',your_slot_value)]
				
class ActionUtterAndSetSlotCuis(Action):
	def name(self):
		return 'action_set_slotCuis'
		
	def run(self, dispatcher, tracker, domain):
		setval = tracker.get_slot("cuisine")
		if (setval !=''):
			your_slot_value = setval
		else:
			your_slot_value = tracker.latest_message.text
			
		cuisine_list=['chinese','mexican','italian','american','south indian','north indian']
		if (your_slot_value == None):
			dispatcher.utter_template("utter_wrong_cuisine",tracker)
		elif (your_slot_value.lower() not in city_list):
			dispatcher.utter_template("utter_wrong_cuisine",tracker)	
		else:
			return [SlotSet('cuisine',your_slot_value)]

class ActionUtterAndSetSlotBud(Action):
	def name(self):
		return 'action_set_slotBud'
		
	def run(self, dispatcher, tracker, domain):
		setval = tracker.get_slot("budget")
		if (setval !=''):
			your_slot_value = setval
		else:
			your_slot_value = tracker.latest_message.text
			
		budget_list=['Lesser than Rs. 300','Rs. 300 to 700','More than 700']
		if (your_slot_value == None):
			dispatcher.utter_template("utter_wrong_budget",tracker)
		elif (your_slot_value.lower() not in city_list):
			dispatcher.utter_template("utter_wrong_budget",tracker)	
		else:
			return [SlotSet('budget',your_slot_value)]
		
		
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
				