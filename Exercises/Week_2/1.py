from threading import Thread
from threading import Lock
import time


F = open('poem.txt','r')
A = F.readlines()

pos = 0
lock = Lock()

def reader(lock):
	global pos
	while pos < len(A):
		lock.acquire()
		print(A[pos])
		lock.release()
		time.sleep(.3)

def iterate(lock):
	global pos
	for y in range(1, (len(A) + 1)):
		lock.acquire()
		pos = y
		lock.release()
		time.sleep(.3)

t = Thread(target=reader, args=(lock, ))
t2 = Thread(target=iterate, args=(lock, ))

t.start()
t2.start()