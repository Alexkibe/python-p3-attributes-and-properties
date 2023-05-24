#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        assert isinstance(name, str) and 0 < len(name) <= 25, "Name must be a string between 1 and 25 characters."
        self.name = name.title()

        assert isinstance(breed, str), "Name must be a string."
        assert breed in APPROVED_BREEDS, "Breed must be in the list of approved jobs."
        self.breed = breed
    
   
    
        
        
    
    
    
    
       
     
    


   
   
    
    
    

    
