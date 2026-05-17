                              ##Concurrency

# import threading
# import time

# def take_order():
#     for i in range(1,4):
#         print(f"Taking order for #{i}")
#         time.sleep(1)

# def brew_chai():
#     for i in range(1,4):
#         print(f"Brewing chai for #{i}")
#         time.sleep(2)

# #creating threads

# order_thread = threading.Thread(target=take_order)
# brew_thread = threading.Thread(target=brew_chai)

# order_thread.start()
# brew_thread.start()

# #wait for both to finish
# order_thread.join()
# brew_thread.join()

# print(f"All orders taken and chai brewed")


#                       ##Multiprocessing
                      
# from multiprocessing import Process
# import time

# def brew_chai(name):
#     print(f"{name} chai served")
#     time.sleep(3)
#     print(f"End of {name} chai brewing")
    
# if __name__ == "__main__": #Each new process re-runs the whole file,That includes creating more processes again,leads to infinite loop / crash
#     chai_makers = [  #Process are created and stored by list comprehension
#         Process(target=brew_chai,args = (f"Chai Maker #{i+1}",)) #Because tuples in Python are defined by commas, not parentheses and args requires tuples
#         for i in range(3) 
#     ]

# #Start all process
#     for p in chai_makers:
#         p.start() #When a process is started then it runs the program again

# #wait for all to complete
#     for p in chai_makers:
#         p.join()

#     print("All chai served")


# 👉 Threading = multiple tasks in the same process (shared memory)
# 👉 Multiprocessing = multiple tasks in separate processes (separate memory)



#                            ##Global interpreter lock (GIL)
# -> Mutex lock when two threads want to access the same memory block 
                           
# import threading
# import time

# def brew_chai():
#     print(f"{threading.current_thread().name} started the brewing...")
#     count = 0
#     for _ in range(100_000_000):
#         count += 1
#     print(f"{threading.current_thread().name} finished brewing , count = {count}")
    
# thread1 = threading.Thread(target=brew_chai,name="Barista-1")
# thread2 = threading.Thread(target=brew_chai,name="Barista-2")
    
# start_time = time.time()
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# end_time = time.time()
# Here the GIL is happening therefore it takes and and the threads cannot work simultaneously    
# print(f"total time taken: {end_time - start_time:.2f} seconds")     

# #Now we can bypass the GIL

# from multiprocessing import Process
# import time

# def crunch_number():                  
#     print(f"Started the count process...")
#     count = 0
#     for _ in range(100_000_000):
#         count += 1 
#     print(f"Ended the count process...with count-> {count}")

# if __name__ == "__main__":
#     start = time.time()
#     p1 = Process(target=crunch_number)
#     p2 = Process(target=crunch_number)
 
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#     end = time.time()
#     print(f"Total time : {end - start:.2f}s")
 
 
# import threading
# import time
# import requests

# def download_urls(url):
#     print(f"Atarting download from {url}")
#     resp = requests.get(url)
#     print(f"Finished downloading from {url},size = {len(resp.content)} bytes")
    
# urls = [
#     "https://httpbin.org/image/jpeg",
#     "https://httpbin.org/image/png",
#     "https://httpbin.org/image/svg"
# ]

# start = time.time()
# threads = []

# for url in urls:
#     t = threading.Thread(target=download_urls,args=(url,))
#     t.start()
#     threads.append(t)
    
# for t in threads:
#     t.join()
    
# end = time.time()
# print(f"All downloads done in {end - start:.2f} seconds")
    

 
###Using locks (mutex)

# import threading
# counter = 0
# lock = threading.Lock()

# def increment():
#     global counter
#     for _ in range(100_00):
#         with lock:        #To prevent overlapping of threads for same value
#             counter += 1
            
# threads = [threading.Thread(target=increment) for _ in range(10)]
# [t.start() for t in threads]
# [t.join() for t in threads]

# print(f"Final answer-{counter}")


#                         ##Queue (Process)
                        
# import threading
# import time

# def cpu_heavy():
#     print(f"Crunching some number..")
#     total = 0
#     for i in range(10**8):
#         total += i
#     print("Done")
    
# start = time.time()
# threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

# for t in threads:
#     t.start()
    
# for t in threads:
#     t.join()
    
# end = time.time()
# print(f"Time taken: {end-start:.2f} s")  #Slow



# from multiprocessing import Process,Queue,Value
# import time

# def cpu_heavy():
#     print(f"Crunching some number..")
#     total = 0
#     for i in range(10**8):
#         total += i
#     print("Done")
    
# start = time.time()

# if __name__ == "__main__":
#     processes = [Process(target=cpu_heavy) for _ in range(2)]
#     for t in processes:
#         t.start()
#     for t in processes:
#         t.join()
#     end = time.time()
#     print(f"Time taken: {end-start:.2f} s")
    
# def prepare_chai(queue):
#     queue.put("Masala Chai is ready")

# def increment(counter):
#     for _ in range(100_00):
#         with counter.get_lock():
#             counter.value += 1

# counter = Value('i',0) #For using lock directly
    
# if __name__ == "__main__":    
    
#     queue = Queue()
#     p = Process(target=prepare_chai,args=(queue,))
#     p.start()
#     p.join()    
#     print(queue.get())