def print_order(name,chai_type): #Parameters here
    print(f"Name : {name} , Chai : {chai_type}")    
print_order("Manas","Ginger")

def calculate_bill(cups,price):
    return cups * price
print("Order for table 2:",calculate_bill(3,15))

def update_order():
    chai_type = "Elaichi"
    def Kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    Kitchen()
    print("After kitchen update:",chai_type)

update_order()    


chai_type = "Plain"
def front_desk():
    def Kitchen():
        global chai_type
        chai_type = "Irani"
    Kitchen()    
    
front_desk()
print(chai_type)


def special_chai(*ingrediants,**extras): # *args(arguments) **kargs(keyvalue arguments)
    
    print("ingrediants: ",ingrediants)
    print("extras: ", extras)
    
special_chai("Cinnamon","Cardmom",sweetner = "Honey",foam = "yes")    


def chai_order(order = []):
    order.append("Masala")
    print(order)
chai_order()    
chai_order()    

def chai_order(order = None):
    if order is None:
        order = []
        order.append("Masala")
    print(order)
chai_order()
chai_order()


                  ###Types of functions
    
#Pure -> Normal function like we modify parameters
#Impure -> Functions in which we change and use the global variables (Not recommended)


##Lamda:Lambda functions in Python are small, anonymous (nameless) functions used for short, one-line operations

chai_types = ["light","kadak","ginger","kadak"]
strong_chai = list(filter(lambda chai: chai != "kadak",chai_types))      
print(strong_chai)

add = lambda a, b: a + b
print(add(2, 3))

students = [("Manas", 85), ("Rahul", 90), ("Amit", 80)]
students.sort(key = lambda x : x[1])
students.reverse()
print(students)


def chai_flavor(flavor = "Masala"):
    """Return the flavor of chai""" #Docstring (always on top of module)
    chai = "ginger"
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)



    
    