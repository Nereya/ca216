import threading
import time
import random

CUSTOMERS = 256
BARBERS = 3
CHAIRS = 15
ARRIVAL_WAIT = 0.5

def wait():
    time.sleep(ARRIVAL_WAIT * random.random())

class Barber(threading.Thread):
    condition = threading.Condition()
    customers = []
    should_stop = threading.Event()

    def run(self):
        while True:
            with self.condition:
                if not self.customers:
                    print "{} is sleeping".format(self)
                    self.condition.wait()
                if self.should_stop.is_set():
                    return
                if not self.customers:
                    print "{} is now awake BUT there is no customers to cut".format(self)
                    continue

                customer = self.customers.pop()
                print"{} is waking up now.".format(self)
            customer.trim()

class Customer(threading.Thread):
    WAIT = 0.05

    def wait(self):
        time.sleep(self.WAIT * random.random())

    def trim(self): 
        print "{} is getting their hair done.".format(self)
        self.wait()
        self.serviced.set()

    def run(self):
        self.serviced = threading.Event()
        with Barber.condition:
            Barber.customers.append(self)
            Barber.condition.notify(1)

        print "{} has gone asleep".format(self)
        self.serviced.wait()
        print"{} is leaving".format(self)

if __name__ == '__main__':
    barbers = []
    for b in range(BARBERS):
        Barber().start()
    all_customers = []
    for c in range(CUSTOMERS):
        wait()
        c = Customer()
        all_customers.append(c)
        c.start()
    for c in all_customers:
        c.join()      
    Barber.should_stop.set()
