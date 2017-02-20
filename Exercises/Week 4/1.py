from threading import Thread
from threading import Lock
import threading
import time


F = open('poem.txt','r')
A = F.readlines()
cv = threading.Condition()
buff = [{} for i in range(10)]
global y
z = 0

def writeFile():
	global A
	global y
	y = 0
	for i in range(0, len(A)):
		cv.acquire()
		if y >= 10:
			y = 0
			buff[y] = A[i]
			y += 1
			cv.notifyAll()
			cv.release()
			time.sleep(.3)
		else:
			buff[y] = A[i]
			y += 1
			cv.notifyAll()
			cv.release()
			time.sleep(.3)


def printFile():
	global A
	global buff
	global y
	global z
	for x in range(0, len(A)):
		cv.acquire()
		if z >= 10:
			z = 0
		while z < y:
			print(buff[z])
			z += 1
		cv.notifyAll()
		cv.release()
		time.sleep(.3)


t = Thread(target=writeFile)
t2 = Thread(target=printFile)

t.start()
t2.start()