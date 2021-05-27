# Semaphores -->> to limit the access to the resources
# It doesn't lock the resources completely but limit them.

import threading
import time

semaphore = threading.BoundedSemaphore(value = 5)           # that allows only 5 accesses at a time

def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10)
    print("{} is releasing now".format(thread_number))
    semaphore.release()

for thread_number in range(1, 11):
    t = threading.Thread(target = access, args = (thread_number,))
    t.start()
    time.sleep(1)


