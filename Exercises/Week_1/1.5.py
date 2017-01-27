from threading import Thread
import time


F = open('poem.txt','r')
A = F.readlines()

pos = 0

def reader():
	global pos
	for x in range(0, len(A)):
		pos = x
		time.sleep(.3)
		print(A[pos])

def iterate():
	global pos
	for y in range(0, len(A)):
		pos = y
		time.sleep(.2)

t = Thread(target=reader)
t2 = Thread(target=iterate)
t.start()
t2.start()