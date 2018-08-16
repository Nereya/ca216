from multiprocessing import Queue
import threading
import time, random

#for when barber is occupied citting customers hair
mutex = threading.Lock()
ARRIVAL_WAIT = 0.05


class Barber(threading.Thread):

	barberWorkingEvent = threading.Event()

	def sleep(self):
		self.barberWorkingEvent.wait()

	def wakeUp(self):
		self.barberWorkingEvent.set()

	def cuttingHair(self, customer):
		#The Barber is busy with a customer
		self.barberWorkingEvent.clear()

		print("{0} is having a haircut".format(customer.name))

		#random hair cutting time 
		randomHairCuttingTime = random.random()
		time.sleep(randomHairCuttingTime)
		print("{0} is done".format(customer.name))

class Customer():
	def __init__(self, name):
		self.name = name


class BarberShop:
	# list of customers waiting for barber
	waitingRoom = []

	def __init__(self, barber, numberOfSeats):
		self.barber = barber
		self.numberOfSeats = numberOfSeats
		print("BarberShop now open with {0} seats.".format(self.numberOfSeats))
		print("Customer minimum wait time is {0}.".format(ARRIVAL_WAIT))

	#barbers ready
	def barbershopOpen(self):
		print("Barber shop is now open")
		trimTimeThread = threading.Thread(target = self.barberCutsHair)
		trimTimeThread.start()


	def enterCustomer(self, customer):
		mutex.acquire()
		print("{0} entered the shop and is looking for a seat.".format(customer.name))

		if len(self.waitingRoom) == self.numberOfSeats:
			print 'Waiting room is full, {0} is leaving.'.format(customer.name)
			mutex.release()
		else:
			print '{0} sat down in the waiting room'.format(customer.name)	
			self.waitingRoom.append(c)	
			mutex.release()
			barber.wakeUp()
		

	#barber is working
	def barberCutsHair(self):
		while True:
			mutex.acquire()

			if len(self.waitingRoom) > 0:
				customer = self.waitingRoom[0]
				del self.waitingRoom[0]
				mutex.release()
				self.barber.cuttingHair(customer)
			else:
				mutex.release()
				print("No more customers, Barber is now sleeping!")
				barber.sleep()
				print("Customer here, Barber is up!")
		

if __name__ == '__main__':

	#to set len of customers 
	numOfCustomers = int(input("Enter number of customers: "))

	barber = Barber()

	barberShop = BarberShop(barber, numberOfSeats=10)
	barberShop.barbershopOpen()

	customers = []	
	for customer in range(1, numOfCustomers+1):
		customers.append("Customer {}".format(customer))

	#each customer in customers visits the barber
	for c in customers:
		c = Customer(c)
		barberShop.enterCustomer(c)
		trimTime = random.random() + ARRIVAL_WAIT
		