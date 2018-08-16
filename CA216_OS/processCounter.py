import multiprocessing
import sys
def printer(continent="Asia"):
	print("The name of the continent is {}".format(continent))
if __name__ == '__main__':
	names = ["America","Europe","Africa"]
	procs = []
	print(procs)
	proc = multiprocessing.Process(target=printer)
	procs.append(proc)
	proc.start()
	print(procs)
	for name in names:
		print("Now processing: {}".format(name))
		proc = multiprocessing.Process(target=printer, args=(name,))
		procs.append(proc)
		proc.start()
		print(procs)
	for proc in procs:
		proc.join()	

