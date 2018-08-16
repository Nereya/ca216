import multiprocessing
import sys
import os
def raise_to_the_power(n, m):
	total = n**m
	pid = os.getpid()
	print("{} ** {} = {} done by process {}".format(n, m, total, pid))
if __name__ == '__main__':
	nums = [(2,1),(2,2),(2,3),(2,4)]
	procs = []
	for num in nums:
		proc = multiprocessing.Process(target=raise_to_the_power, args=(num))
		procs.append(proc)
		proc.start()
		print(procs)

	for proc in procs:
		proc.join()	
#raise_to_the_power()	