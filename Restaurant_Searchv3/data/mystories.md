## Story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - action_set_slotLoc
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - action_set_slotCuis
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slotEml	
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
	- utter_send_email	
	- utter_goodbye
	- action_restart

## Story 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - action_set_slotLoc
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - action_set_slotCuis
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* deny
	- utter_goodbye
	- action_restart	

## Story 3
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai","cuisine": "mexican"}
    - action_set_slotLoc
    - slot{"location": "Mumbai"}
    - action_set_slotCuis
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "Between 300 to 700"}
    - action_set_slotBud
    - slot{"budget": "Between 300 to 700"}
    - action_restaurant
    - utter_email
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slotEml	
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
	- utter_send_email	
	- utter_goodbye
	- action_restart	
 
 ## Story 4
* greet
    - utter_greet
* restaurant_search{"location": "Delhi","cuisine": "italian"}
    - action_set_slotLoc
    - slot{"location": "Pune"}
    - action_set_slotCuis
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - action_set_slotBud
    - slot{"budget": "Rs. 300 to 700"}
    - action_restaurant
    - utter_email
* deny
	- utter_goodbye
	- action_restart	

## Story 5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - action_set_slotLoc
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - action_set_slotCuis
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* affirm{"emailid": "nareshdogra@rediffmail.com"}
	- utter_ask_emailid
    - action_set_slotEml	
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
	- utter_send_email	
	- utter_goodbye
	- action_restart
	
## Story 6
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore","cuisine": "south indian"}
    - action_set_slotLoc
    - slot{"location": "Bangalore"}
    - action_set_slotCuis
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - action_set_slotBud
    - slot{"budget": "Lesser than Rs. 300"}
    - action_restaurant
    - utter_email
* affirm{"emailid": "nareshdogra@rediffmail.com"}
	- utter_ask_emailid
    - action_set_slotEml	
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
	- utter_send_email	
	- utter_goodbye
	- action_restart
	

## Story 7
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - action_set_slotLoc
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine	
* restaurant_search{"cuisine": "american"}
    - action_set_slotCuis
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "> 700"}
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slotEml	
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
	- utter_send_email	
	- utter_goodbye
	- action_restart

## Story 8
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - action_set_slotLoc
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine	
* restaurant_search{"cuisine": "chinese"}
    - action_set_slotCuis
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - action_set_slotBud
    - slot{"budget": "Rs. 300 to 700"}
    - action_restaurant
    - utter_email
* deny
	- utter_goodbye
	- action_restart	
	