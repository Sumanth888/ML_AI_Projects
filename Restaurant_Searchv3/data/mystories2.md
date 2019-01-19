## Story 1
* greet
    - utter_greet
* restaurant_search	
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "Pune"}
    - action_set_slotLoc
    - slot{"location": "Pune"}
    - action_set_slot
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "italian"}
    - action_set_slotCuis
    - slot{"cuisine": "italian"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "More than 700"}
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slot
    - action_restaurant_eml
	- utter_goodbye
	- action_restart
    - export
	
## Story 2
* greet
    - utter_greet
* restaurant_search	
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "Delhi"}
    - action_set_slotLoc
    - slot{"location": "Delhi"}
    - action_set_slot
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "italian"}
    - action_set_slotCuis
    - slot{"cuisine": "italian"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "More than 700"}
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email                     	  
* deny
	- utter_goodbye
	- action_restart
    - export	

## Story 3
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai","cuisine": "mexican"}
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "Rs. 300 to 700"}
    - action_set_slotBud
    - slot{"budget": "Rs. 300 to 700"}
    - action_restaurant
    - utter_email
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slot
    - action_restaurant_eml
	- utter_goodbye
	- action_restart
    - export	
 
## Story 4
* greet
    - utter_greet
* restaurant_search{"location": "Delhi","cuisine": "italian"}
    - slot{"location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "Rs. 300 to 700"}
    - action_set_slotBud
    - slot{"budget": "Rs. 300 to 700"}
    - action_restaurant
    - utter_email
* deny
	- utter_goodbye
	- action_restart
    - export	


## Story 5
* greet
    - utter_greet
* restaurant_search	
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "Bangalore"}
    - action_set_slotLoc
    - slot{"location": "Bangalore"}
    - action_set_slot
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "north indian"}
    - action_set_slotCuis
    - slot{"cuisine": "north indian"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "More than 700"}
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* affirm
    - action_set_slot
    - slot{"requested_slot": "emailid"}
* restaurant_search
    - action_set_slotEml
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - export

## Story 6
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore","cuisine": "south indian"}
    - slot{"location": ["Bangalore"]}
    - slot{"cuisine": "south indian"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - action_set_slotBud
    - slot{"budget": "Lesser than Rs. 300"}
    - action_restaurant
    - utter_email
* affirm
    - action_set_slot
    - slot{"requested_slot": "emailid"}
* restaurant_search
    - action_set_slotEml	
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
	- utter_goodbye
	- action_restart
    - export	
	

## Story 7
* greet
    - utter_greet
* restaurant_search	
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "Kolkata"}
    - action_set_slotLoc
    - slot{"location": "Kolkata"}
    - action_set_slot
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "american"}
    - action_set_slotCuis
    - slot{"cuisine": "american"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "More than 700"}
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slot
    - action_restaurant_eml
	- utter_goodbye
	- action_restart
    - export	

	
## Story 8
* greet
    - utter_greet
* restaurant_search	
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_set_slot
    - slot{"requested_slot": "cuisine"}	
* restaurant_search{"cuisine": "chinese"}
    - action_set_slotCuis
    - slot{"cuisine": "chinese"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "Rs. 300 to 700"}
    - action_set_slotBud
    - slot{"budget": "Rs. 300 to 700"}
    - action_restaurant
    - utter_email
* deny
	- utter_goodbye
	- action_restart
    - export	
	