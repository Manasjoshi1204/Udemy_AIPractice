kettle_boiled = input("Kettle Boiled? ").lower() == "true"
if kettle_boiled:
    print("Kettle Done!")
else:
    print("Not Done!")
    
    
snack = input("Enter your snack: ").lower()
if snack == "samosa" or snack == "cookies":
    print(f"Good choice of {snack}")  
elif snack.isdigit() == True:
    print("Not a proper input")     
else:
    print("Unavailable")
    

device_status = input("Device Status (Offline/Active): ").lower()
if device_status == "active":
    temperature = int(input("Temperature: "))
    if temperature > 35:
        print("High Temperature: ")
    else:
        print("Temperature Normal")
else:
    print("Device is offline!")
    
              ###Ternary Operator
    
order_amount = int(input("Enter order amount: "))
delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fees is {delivery_fees}")  

               ###Match keyword (switch case)  

seat_type = input("Enter seat type: ").lower()
match seat_type:
    case "sleeper":
        print("Something")
    case "luxury":
        print("jingg")
    case "general":
        print("forsaken")
    case _:
        print("Invalid seat-type")
        
        
    
           
          


    