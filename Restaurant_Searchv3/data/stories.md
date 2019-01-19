## Generated Story 7585585777738663773
* greet
    - utter_greet
* restaurant_search
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search{"location": "mumbai"}
    - slot{"location": ["mumbai"]}
    - action_set_slot
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_set_slot
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_senton_email
* affirm
    - utter_ask_emailid
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slotEml
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - action_restart

## Generated Story 412522349573410301
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": ["Delhi"]}
    - action_set_slot
    - slot{"location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_senton_email
* affirm
    - utter_ask_emailid
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slotEml
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - action_restart
    
## Generated Story -4653823490529546206
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": ["mumbai"]}
    - action_set_slot
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_set_slot
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "budget"}
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_senton_email
* affirm
    - utter_ask_emailid
* affirm{"emailid": "nareshdogra@rediffmail.com"}
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_set_slotEml
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - action_restart
    
## Story 1
* greet
    - utter_greet
* restaurant_search    
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search
    - slot{"location": "Pune"}
    - action_set_slot
    - slot{"location": "Pune"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - slot{"cuisine": "italian"}
    - action_set_slot
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "budget"}
* restaurant_search
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_senton_email
* affirm
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - action_restart
    
## Story 2
* greet
    - utter_greet
* restaurant_search
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search
    - slot{"location": "Delhi"}
    - action_set_slot
    - slot{"location": "Delhi"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - slot{"cuisine": "italian"}
    - action_set_slot
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "budget"}
* restaurant_search
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_senton_email
* deny
    - utter_goodbye
    - action_restart

## Story 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai"}
    - slot{"location": ["Mumbai"]}
    - slot{"cuisine": "Mexican"}
    - action_set_slot
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"requested_slot": "budget"}
* restaurant_search
    - slot{"budget": "Rs. 300 to 700"}
    - action_restaurant
    - utter_senton_email
* affirm
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - action_restart
 
## Story 4
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Delhi"}
    - slot{"location": ["Delhi"]}
    - slot{"cuisine": "Mexican"}
    - action_set_slot
    - slot{"location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"requested_slot": "budget"}
* restaurant_search    
    - slot{"budget": "Rs. 300 to 700"}
    - action_restaurant
    - utter_senton_email
* deny
    - utter_goodbye
    - action_restart


## Story 5
* greet
    - utter_greet
* restaurant_search
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search
    - slot{"location": "Bangalore"}
    - action_set_slot
    - slot{"location": "Bangalore"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - slot{"cuisine": "north indian"}
    - action_set_slot
    - slot{"cuisine": "north indian"}
    - slot{"requested_slot": "budget"}
* restaurant_search
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_senton_email
* affirm
    - utter_ask_emailid
* restaurant_search
    - action_set_slotEml
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - action_restart


## Story 6
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Bangalore"}   
    - slot{"location": ["Bangalore"]}
    - slot{"cuisine": "south indian"}
    - action_set_slot
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "south indian"}
    - slot{"requested_slot": "budget"}
* restaurant_search
    - slot{"budget": "Lesser than Rs. 300"}
    - action_restaurant
    - utter_senton_email
* affirm
    - utter_ask_emailid
* restaurant_search
    - action_set_slotEml
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - action_restart


## Story 7
* greet
    - utter_greet
* restaurant_search
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search
    - slot{"location": "Kolkata"}
    - action_set_slot
    - slot{"location": "Kolkata"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - slot{"cuisine": "american"}
    - action_set_slot
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "budget"}
* restaurant_search
    - slot{"budget": "More than 700"}
    - action_restaurant
    - utter_senton_email
* affirm
    - slot{"emailid": "nareshdogra@rediffmail.com"}
    - action_restaurant_eml
    - utter_goodbye
    - action_restart


## Story 8
* greet
    - utter_greet
* restaurant_search
    - action_set_slot
    - slot{"requested_slot": "location"}
* restaurant_search
    - slot{"location": "Kolkata"}
    - action_set_slot
    - slot{"location": "Kolkata"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - slot{"cuisine": "chinese"}
    - action_set_slot
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* restaurant_search
    - slot{"budget": "Rs. 300 to 700"}
    - action_restaurant
    - utter_senton_email
* deny
    - utter_goodbye
    - action_restart