from threading import Thread
from threading import Lock
import threading
import time


F = open('poem.txt','r')
A = F.readlines()

pos = 0
cv = threading.Condition()
number = 0

def reader():
	global pos
	global number
	while number != 2:
		cv.acquire()
		print(A[pos])
		cv.notifyAll()
		cv.release()
		time.sleep(.5)
	print('Thread 1 closing...')	

def iterate():
	global pos
	global number
	while number != 2:
		for y in range(1, (len(A))):
			if number == 2:
				break
			else:
				cv.acquire()
				pos = y
				cv.notifyAll()
				cv.release()
				time.sleep(.5)
	print('Thread 2 closing...')	

def condition():
	global number
	number = int(input())
	if number == 1:
		cv.acquire()
		print('Pausing output')
		cv.wait()
		number = int(input())
	if number == 0:
		print('Resuming output')
		cv.notifyAll()
		cv.release()
		number = int(input())	
	if number == 2:
		print ('Exiting')		
		
				

t = Thread(target=reader)
t2 = Thread(target=iterate)
t3 = Thread(target=condition)

t.start()
t2.start()
t3.start()
