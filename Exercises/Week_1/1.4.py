from threading import Thread
import time


F = open('poem.txt','r')
A = F.readlines()

global pos

def reader():
	global pos
	for x in range(0, len(A)):
		pos = x
		print(A[pos])
		time.sleep(.3)

t = Thread(target=reader)
t.start()
t.join()
