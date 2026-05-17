               ###FOR loop

for i in range(1,11):
    print(f"Serving chai to Token: {i+1}")
    
orders = ["Manas","Joshi","Noob"]
for name in orders:
    print(f"Order ready for: {name}")

              ###Enumerate -> It lets you loop through a list AND get the index + value at the same time
    
menu = ["Green","lemon","Spiced","Mint"]

for idx,item in enumerate(menu,start=1):
    print(f"{idx} : {item} chai")
    
for i in range (len(menu)):
    print(f"{i+1} : {menu[i]} chai")


                ###ZIP (for iterating 2 lits at once)
                
names = ["Manas","Joshi","Noob"]
bills = [100,200,300]

for name,amount in zip(names,bills):
    print(f"{name} : {amount}")



                 ### WHILE LOOP

temperature = 40
while temperature <= 100:
    print(f"Temperature : {temperature}")
    temperature += 15          
print("Temperature over 100")      



                ###Continue and Break
                
flavours = ["Ginger","Out of stock","Lemon","Discontinued","Tulsi"]
for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} chai")
print(f"Outside Loop")    


staff = [("Manas",19),("Joshi",18),("Noob",12)]
for name,age in staff:
    if age <= 18 :
        print(f"{name} is eligible")
        break
else:
    print("No one is eligible")

                ###Walrus Operator

value = 13
if(remainder := value%5): #WALRUS OPERATOR (:=)
    print(f"Not divisble,remainder: {remainder}")
    
available_sizes = ["small","medium","large"]

if(requested_size := input("Enter Size: ").lower()) in available_sizes:
    print(f"Yes {requested_size} size is available")
else:
    print("Not available")

            ###Using dictonary instead of Else-if


users = [
    {"id": 1,"total":100,"coupon":"P20"},
    {"id": 2,"total":150,"coupon":"F10"},
    {"id": 3,"total":80,"coupon":"P50"},
]

discounts = {
    "P20": (0.2,0),
    "F10" : (0,10),
    "P50" : (0.5,0)
}

for user in users:
    percent,fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    print(f"Dicount for user {user['id']} is {discount}")
    
