from threading import Thread
import os
import math


def izracunavanje():
	for i in range(0, 13000000):
		math.sqrt(i)


threads = []

print('koliko cpuova toliko tredova %s' % os.cpu_count())
for i in range(os.cpu_count()):
	print('%s out of %s' % (i + 1, os.cpu_count()))
	threads.append(Thread(target=izracunavanje))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()