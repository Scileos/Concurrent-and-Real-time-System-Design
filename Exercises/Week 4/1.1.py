from threading import Thread
from threading import Lock
import threading
import time


F = open('poem.txt','r')
A = F.readlines()

cv = threading.Condition()
controlInt = 0

def funcA():
	global controlInt
	cv.acquire()
	if controlInt == 0:
		print('Thread 1 running, controlInt = ', controlInt)
		controlInt += 1
		time.sleep(.5)
		cv.notifyAll()
		cv.release()
	else:
		time.sleep(.5)
		cv.notifyAll()
		cv.release()

def funcB():
	global controlInt
	cv.acquire()
	if controlInt == 1:
		print('Thread 2 running, controlInt = ', controlInt)
		controlInt += 1
		time.sleep(.5)
		cv.notifyAll()
		cv.release()
	else:
		time.sleep(.5)
		cv.notifyAll()
		cv.release()

def funcC():
	global controlInt
	cv.acquire()
	if controlInt == 2:
		print('Thread 3 running, controlInt = ', controlInt)
		controlInt += 1
		time.sleep(.5)
		cv.notifyAll()
		cv.release()
	else:
		time.sleep(.5)
		cv.notifyAll()
		cv.release()

def funcD():
	global controlInt
	cv.acquire()
	if controlInt == 3:
		print('Thread 4 running, controlInt = ', controlInt)
		controlInt += 1
		time.sleep(.5)
		cv.notifyAll()
		cv.release()
	else:
		time.sleep(.5)
		cv.notifyAll()
		cv.release()


t = Thread(target=funcA)
t2 = Thread(target=funcB)
t3 = Thread(target=funcC)
t4 = Thread(target=funcD)

t.start()
t2.start()
t3.start()
t4.start()
		
				


