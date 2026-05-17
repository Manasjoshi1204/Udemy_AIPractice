# Async def-> declare a co-routine (special function that can be paused)
# await -> Pauses execution until the result is ready
# asyncio -> build inmpython library
# event loop -> The engine that runs and schedule co-routines in python  

import asyncio

async def brew_chai():
    print("Brewing Chai...")
    await asyncio.sleep(2) #it does not block the main thread like time.sleep()
    print("Chai is Ready!")
    
asyncio.run(brew_chai())

# import asyncio
import time

async def brew(name):
    print(f"Brewing {name} chai...")
    # await asyncio.sleep(2)
    time.sleep(2)
    print(f"{name} is ready...")

async def main(): 
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Ginger Chai"),
        brew("Lemon Chai"),
    )
    
asyncio.run(main()) #All function is printed at same time 


# import asyncio
import aiohttp

async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")
        
async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks) # * -> to unpack the list for gather
        
asyncio.run(main())


                        #Threads with asyncio
# import asyncio
# import time
from concurrent.futures import ThreadPoolExecutor #Like gather() but for threads

def check_stock(item):
    print(f"Checking item in store...")
    time.sleep(3) #Blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop() #This gets the currently active asyncio event loop
    with ThreadPoolExecutor() as pool:   #using with because threads are resources which need to be cleaned after use and threadpoolexecutor makes new threads 
        result = await loop.run_in_executor(pool,check_stock,"Masala Chai") #run_in_executor let asyncio run async funtion in another thread,we dont touch main thread therfore no blocking
        print(result) 

asyncio.run(main())

                        ###Multiprocess with asyncio
#import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"{data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool: #Makes new proccesses
        result = await loop.run_in_executor(pool,encrypt,"credit_card_1234") 
        print(result)

if __name__ == "__main__":   
    asyncio.run(main())
    

import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health")
    
async def fetch_orders():
    await asyncio.sleep(3)
    print("Order fetched")
    
threading.Thread(target=background_worker,daemon=True).start()
asyncio.run(fetch_orders())    


                       #Daemon and Non-Daemon Threads
#Daemon threads are background threads that automatically terminate when the main program exits. They are typically used for tasks that should run in the background and do not need to prevent the program from exiting. Non-daemon threads, on the other hand, are foreground threads that keep the program running until they complete their tasks. If a non-daemon thread is still running when the main program tries to exit, the program will wait for that thread to finish before it can exit.                       
                       
import threading
import time

def monitor():
    while True:
        print("Monitoring system health...")    
        time.sleep(2)
        
t = threading.Thread(target=monitor,daemon=True)#Daemon thread will automatically stop when main program exits     
t.start()
print("Main program done")

                          
###Profiling-> python -m cProfile -s time (file name) --->PYSPY,VPROF

                   ###Race Conditioning 
#Where 2 threads race each other to update the value 
                   
import threading
chai_stock = 0

def re_stock():
    global chai_stock
    for _ in range(100_000):
        chai_stock += 1
        
threads = [threading.Thread(target=re_stock) for _ in range(2)]
for t in threads : t.start()                      
for t in threads : t.join()                      

print("Chai stock: ",chai_stock)

                         ###Deadlock
                         
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def brew_1():
    with lock_a:
        print("Brew_1 acquired lock a")
        with lock_b:
            print("Brew_1 acquired lock b")
            
def brew_2():
    with lock_b:
        print("Brew_2 acquired lock b")
        with lock_a:
            print("Brew_2 acquired lock a")
            
t1 = threading.Thread(target=brew_1)
t2 = threading.Thread(target=brew_2)

t1.start()
t2.start()
