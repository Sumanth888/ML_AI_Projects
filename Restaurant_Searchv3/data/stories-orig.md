## Generated Story -3096322100342415882
* greet
    - utter_greet
* restaurant_search
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search
    - action_set_slotLoc
    - slot{"location": "Pune"}
    - action_set_slot
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_set_slot
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* goodbye
    - action_set_slotBud
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* affirm
    - action_set_slot
    - slot{"requested_slot": "emailid"}
* restaurant_search
    - action_set_slotEml
    - slot{"emailid": "raodeepthi21@gmail.com"}
    - action_restaurant_eml
    - slot{"location": "Pune"}
    - utter_goodbye
    - export
	
## Generated Story 7904787983750552661
* greet
    - utter_greet
* restaurant_search
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "Pune"}
    - slot{"location": ["Pune"]}
    - action_set_slotLoc
    - action_set_slot
    - slot{"location": "Pune"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - action_set_slotCuis
    - slot{"cuisine": "italian"}
    - action_set_slot
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_email
* affirm
    - action_set_slot
    - slot{"requested_slot": "emailid"}
* restaurant_search
    - action_set_slotEml
    - slot{"emailid": "sachinmv88@gmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - export

	## Generated Story 3123330545366563598
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": ["mumbai"]}
    - action_set_slot
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_restaurant
    - utter_email
* affirm
    - action_set_slot
    - slot{"requested_slot": "emailid"}
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - export
