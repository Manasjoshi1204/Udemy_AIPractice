#Comprehensions are a concise way to create lists,sets,dictionaries or generators in a single 

              ###List comprehension

#Syntax -> [expression for item in iterable if condition]

menu = [
    "Masala Chai",
    "Iced Lemon tea",
    "Green Tea",
    "Iced Peach tea",
    "Ginger tea"
]
iced_tea = [tea for tea in menu if "Iced" in tea]
big_tea = [tea for tea in menu if len(tea)>10]
print(iced_tea)
print(big_tea)


                ###Set comprehension
                
#Syntax -> {expression for item in iterable if condition}

favourite_chai = [
    "Masala Chai","Green Tea","Masala Chai",
    "Lemon Tea","Green Tea","Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chai}
print(unique_chai)

recipes = {
    "Masala Chai" : ["Ginger","cardamom","clove"],
    "Elaichi Chai" : ["cardamom","milk"],
    "Spicy Chai" : ["Ginger","black pepper","clove"]
}

 


                 ###Dict Comprehension
                 
#Syntax -> {expression(key-value) for item in iterable if condition}

tea_prices_inr = {
    "Masala Chai"  : 40,
    "Green Tea" : 50,
    "Lemon Tea" : 200
}

tea_prices_usd = {chai:price/80 for chai,price in tea_prices_inr.items()}
print(tea_prices_usd)


                  ###Generator Comprehension
                  
#Syntax -> (expression for item in iterable if condition) (Gives output as stream not like once in lists)

daily_sales = [5,10,12,7,3,8,9,15]
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)

#It is used for memory efficient operations like sum,avg so it does not give a list it send streams of data thats why it is used for these operations