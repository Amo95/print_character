from Queue import Queue
import time
import random

class Simulate:

    def simulate(self, till_show, max_time):
        pq = Queue()
        tix_sold = list()

        for i in range(100):
            print(pq.enqueue(f"person: {i}"))

        t_end = time.time() + till_show
        now = time.time()

        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold
            
