from multiprocessing import Process, Queue
import os
sentinel = -1		#handy to make the program stop.

def creator(data, q):
	
	print("Creating data and putting it on the queue")
	for item in data:
		q.put(item)			#adds the items in data to a Queue

def consumer(q):

	''' Consumer works on the data in the Queue made in the method above
		In this case we double each item
	'''

	while True:
		data = q.get()
		print("data found to be processed: {}".format(data))
		processed = data*2
		print("Data doubled is: {} \nProcess ID: {}".format(processed, os.getpid()))

		if data is sentinel:
			break 			#Stop the program
if __name__ == '__main__':

	q = Queue()					
	data = [1,2,3,4,5,-1]
	proc_one = Process(target=creator, args=(data, q))
	proc_two = Process(target=consumer, args=(q,))
	proc_one.start()
	proc_two.start()

	q.close()			# Close the queue
	q.join_thread()		# Kill the queue management threads 

	proc_one.join()		# Kill producer
	proc_two.join()		# Kill consumer

