                ###Generators
                
#Generators are like functions in Python that produce values one at a time using the yield keyword, instead of returning all values at once.                

#You save memory,sometimes we dont want results immediately (lazy evaluation) there we use generators (memory Efficiency)

def serve_chai():
    yield "Cup 1 : Masala Chai"
    yield "Cup 2 : Ginger Chai"
    yield "Cup 3 : Elaichi Chai"
    
stall = serve_chai()

for cup in stall:
    print(cup)  

#next() -> next() is used to manually control iteration, while a for loop automatically handles iteration.
#next() is used to retrieve the next value from an iterator or generator. In the case of generators, it resumes execution until the next yield statement.

print(next(stall))
print(next(stall))    
print(next(stall))


###Infinite Generators

def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1
        
refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))
    
for _ in range(6):
    print(next(user2))
    
    
###Send data to Generators

def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield #Stops the program for input
    while True:
        print(f"Preparing : {order} ")
        order = yield #To stop the program for next input
        
stall = chai_customer()
next(stall) #Start the genrator
stall.send("Masala Chai")
stall.send("Lemon Chai")


##Yield from and close

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    
def imported_chai():
    yield "Matcha"
    yield "Oolong"
    
def full_menu():
    yield from local_chai()
    yield from imported_chai()
    
for chai in full_menu():
    print(chai)
    
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order!"
    except:
        print("Stall closed,No more chai!")
        
stall = chai_stall()
print(next(stall))
stall.close() #cleanup of memory



                 ###Decorators
#Decorators are functions that modify or extend the behavior of another function without changing its actual code

from functools import wraps

def my_decorator(func):
    
#We need a wrapper function because we want to execute additional code before and after the original function when it is called, not when it is decorated.
    
    @wraps(func) ##For correct function name
    def wrapper():
        print("Before Func runs:")
        func() #Otherwise it will run when outside the wrapper
        print("After Func runs:")
    return wrapper

@my_decorator
def greet():
    print("Hello")
    
greet()
print(greet.__name__)


###Logging Decorator

from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args,**kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type,milk = "no"):
    print(f"Brewing {type} Chai and milk status {milk}")
    
brew_chai("Masala")



###Authorization Decorator
from functools import wraps
def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied: Admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Access granted!")
    
access_tea_inventory("user")
access_tea_inventory("admin")
