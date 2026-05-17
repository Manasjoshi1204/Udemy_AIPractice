                        
Mutables = "The identity(id) can be changed" #Append can be done but id remains same this means we can change the main items in the id we created at start                        
Immutables = "The identity cannot be changed,never refer to value or type as they can be changed"# this means we we replace the object then new id will be created                          
                        
                        ###Integers

milk_litres = 7
servings = 4
milk_per_serving = milk_litres/servings
milk_per_serving = milk_litres//servings
#print(f"Milk per serving is {milk_per_serving}")

total_tea_leaves = 1_000_000_000_000
#print(total_tea_leaves)


                         ###Boolean

is_Boiling = True
stri_count = 5 
total_actions = is_Boiling + stri_count #UPCASTING

milk_present = 0
milk_present = None
#print(bool(milk_present)) #Converts int to bool


                          ###Float
import sys 
from fractions import Fraction
from decimal import Decimal as D
#print(sys.float_info)


                          ###Strings
                          
chai_description = "Aromatic And Bold"

# print(f"First Word: {chai_description[0:8]}")
# print(f"Skip Word: {chai_description[0:8:2]}")
# print(f"First Word: {chai_description[:8]}")
# print(f"Last Word: {chai_description[12:]}")
# print(f"Reverse Word: {chai_description[::-1]}")
# print(f"Reverse Single Word: {chai_description[0:8][::-1]}")
# print(f"Reverse Single Word: {chai_description[7::-1]}")

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
# print(f"Encoded label: {encoded_label}")
# print(f"Non-encoded text: {label_text}")
# decoded_label = encoded_label.decode("utf-8")
# print(f"Decoded label: {decoded_label}")



                        ###Tuples
                        
masala_spices = ("cardamom","cinnamon","cloves")
(spice1,spice2,spice3) = masala_spices
#print(f"Main Masala spices: {spice1},{spice2},{spice3}")                        

ginger_ratio , cardamom_ratio = 2,1 #Because of tuples (2,1) 
ginger_ratio , cardamom_ratio = cardamom_ratio , ginger_ratio 

#print(f"Is Ginger in Masala_spices? {'ginger' in masala_spices}")


                        ###Lists (Mutables from here)
                        
ingredients = ["water","milk","black tea"]
ingredients.append("sugar")           
ingredients.remove("water")
#print(ingredients)

spice_option = ["ginger","cardamom"]
ingredients.extend(spice_option)
#print(ingredients)             
ingredients.insert(2,"water")     
#print(ingredients)                   
last_added = ingredients.pop()
ingredients.reverse()
ingredients.sort()

lst = [10, 20, 30, 40]
del lst[1]   # remove element at index 1
#print(lst)

sugar_levels = [1,2,3,4]
maxi = max(sugar_levels)
mini = min(sugar_levels)
#print(maxi) 

from operator import itemgetter
students = [("Manas", 85), ("Rahul", 90), ("Amit", 80)]
students.sort(key=itemgetter(1))
#print(students)

raw_spice_data = bytearray(b"CINNAMON") #Normal bytes objects are immutable (you cannot change them after creation).bytearray solves this by allowing modification.
#print(f"Bytes: {raw_spice_data}")
new_spice_data = raw_spice_data.replace(b"CINNA",b"CARD")
#print(f"Bytes: {new_spice_data}")

raw_spice_data = bytearray(b"CINNAMON") #Proof that bytearray is mutable
raw_spice_data[0:5] = b"CARD"   # in-place change
#print(raw_spice_data)
#print(id(raw_spice_data))

#bytearray is the mutable version of bytes, similar to how a list is mutable and a tuple is immutable


                             ###Sets or FrozenSets (No indexing->unordered)
                             #Because sets use a concept called hashing (internal storage for fast lookup), not indexing.So Python stores elements based on hash values, not positions.
                             
essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices
common_spices = essential_spices & optional_spices
onlyin_essential_spices = essential_spices - optional_spices
unique_spices = all_spices - common_spices
#print(all_spices,common_spices,onlyin_essential_spices,unique_spices)

s = {1, "hello", 3.5}
s = {}        #This is a dictionary
s = set()     #Correct way to create empty set

s = {1, 2}
s.add(3)
s.update([4, 5, 6]) #Multiple adding
s.remove(2)   # error if not present
s.discard(10) # no error         

s = {10, 20, 30} #To convert to list for indexing
lst = list(s)
#print(lst[1])   # works          


                        ###Dictionary
                        
chai_order = dict(type="Masala Chai",size="Large",sugar=2)
#print(f"Chai order: {chai_order}")                                 

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
#print(f"Chai_base: {chai_recipe["base"]}")
del chai_recipe["liquid"]

d = {"a": [1, 2, 3]}
d["a"].clear()
#print(d)

# print(chai_order.keys())
# print(chai_order.values())
# print(chai_order.items())

extra_spices = {"cardamon" : "crushed","ginger":"sliced"}
chai_order.update(extra_spices)
#print(f"Updated Chai order: {chai_order}")

chai_note = chai_order.get("note","NO NOTE ")
#print(f"Customer Note is: {chai_note}")



                        ###Collections

#import arrow
#brewing_time = arrow.utcnow()
#brewing_time.to("Europe/Rome")

from collections import namedtuple
chaiProfile = namedtuple("ChaiProfile",["Flavor","aroma"])


