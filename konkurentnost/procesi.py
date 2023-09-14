import multiprocessing
from multiprocessing import Process, freeze_support
import os
import math

def izracunavanje(event):
	for i in range(0, 17000000):
		math.sqrt(i)

def run():
	freeze_support()
	processes = []

	print('koliko cpuova toliko procesa %s' % os.cpu_count())
	for i in range(os.cpu_count()):
		print('%s out of %s' % (i + 1, os.cpu_count()))
		processes.append(Process(target=izracunavanje, args=[ev]))

	for process in processes:
		process.start()

	for process in processes:
		process.join()

if __name__ == '__main__':
	run()
