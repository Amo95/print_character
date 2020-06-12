import time
import random

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == list()

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):    
        tix_sold = []

        for i in range(100):
            self.enqueue("person: " + str(i))

        t_end = time.time() + till_show
        now = time.time()

        while now < t_end and not self.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = self.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold


new = Queue()
sold = new.simulate_line(20, 2)
print(sold)
