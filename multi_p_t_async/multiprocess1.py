
from multiprocessing import Process
import os
import math


def calc():
  for i in range(0, 4000000):
    math.sqrt(i)

processes = []

for i in range(os.cpu_count()):
  print('registering process %d' % i)
  processes.append(Process(target=calc))

for process in processes:
  process.start()

for process in processes:
  process.join()





'''
from multiprocessing import Process
import os
import time

def square_numbers():
  for i in range(100):
    i * i
    time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

# create processes
for i in range(num_processes):
  p = Process(target=square_numbers)
  processes.append(p)

print(f"p looks like {p}")

# start
for p in processes:
  p.start()

# join
for p in processes:
  p.join()

print('end main')

'''