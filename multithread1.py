
from threading import Thread
import os
import math


def calc():
  for i in range(0, 4000000):
    math.sqrt(i)

threads = []

for i in range(os.cpu_count()):
  print('registering thread %d' % i)
  threads.append(Thread(target=calc))

for thread in threads:
  thread.start()
  print(f"starting thread {thread}")

for thread in threads:
  thread.join()
  print(f"joining thread {thread}")





'''
from threading import *
from time import sleep

class Hello(Thread):
  def run(self):
    for i in range(5):
      print("Hello")
      sleep(1)

class Hi(Thread):
  def run(self):
    for i in range(5):
      print("Hi")
      sleep(1)

t1 = Hello()
t2 = Hi()


t1.run()
t2.run()


t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("bye")

'''


