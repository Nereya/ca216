import multiprocessing
import time 
from multiprocessing import current_process
import os 
def doubler(num):
	result = num * 2
	pid = os.getpid()		#gets you the process ID
	p_name = current_process().name
	#time.sleep(6)
	print("{} doubled is  {} done by process {}".format(num, result, p_name))
if __name__ == '__main__':
	nums = [1,2,3,4,5,6]
	procs = []
	for index, num in enumerate(nums):
		print(index, num)
		proc = multiprocessing.Process(target=doubler, args=(num,))
		procs.append(proc)
		proc.start()
		
	for proc in procs:
		proc.join()	
	

