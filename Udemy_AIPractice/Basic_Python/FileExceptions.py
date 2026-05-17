#Try/Except

chai_menu = {"Masala":30,"ginger":40}
try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exists")
    
print("Hello")

def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ",e)
    else: 
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")
        
serve_chai("Masala")
serve_chai("unknown")


def process_order(item,quantity):
    try:
        price = {"masala":20}[item] #Making a dict and seeing that key == item then storing its value in price
        if not isinstance(quantity,(int,float)):
            raise TypeError("Quantity must be in number")
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry Chai is not on menu")
    except TypeError as e:
        print(e)
    
process_order("ginger",2)
process_order("masala","two")


#Raise your own errors

def brew_chai(flavor):
    if flavor not in ["masala","ginger","elaichi"]:
        raise ValueError("Unsupported chai error")
    print(f"Brewing {flavor} chai...")
    
brew_chai("mint")
    
#Custom exceptions

class OutofIngredientsError(Exception):
    print("Sahi krle bhsdk")

def make_chai(milk,sugar):
    if milk == 0 or sugar == 0:
        raise OutofIngredientsError("Missing milk ir sugar")
    print("Chai is ready")
    
make_chai(0,1)


                            #Mini project

class InvalidChaiError(Exception): pass #just our own exception name

def bill(flavor,cup):
    menu = {"masala":20,"ginger":40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cup,int):
            raise TypeError("Use numbers")
        total = menu[flavor] * cup
        print(f"Your bill for {cup} of flavor {flavor} is {total}")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thanks")
        
bill("mint",2)
bill("masala","three")
bill("ginger",4)


                            ###File Handling
                            
file = open("order.txt","w") #(file.__enter__() is called)
try:
    file.write("Masala Chai - 2 cups")
finally:
    file.close()   #(file.__exit__() is called)
    
with open("order.txt","w") as file:
    file.write("Ginger Tea - 4 cups")
