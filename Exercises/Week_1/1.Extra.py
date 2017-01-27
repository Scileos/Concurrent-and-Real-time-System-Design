from threading import Thread
import time


F = open('poem.txt','r')
A = F.readlines()

pos = 0
percentage = 0

def reader():
	global pos
	global percentage
	lines = int(len(A) * ((percentage/100)))
	for x in range(0, lines) :
		pos = x
		time.sleep(.3)
		print(A[pos])

def menu():
	global percentage
	selection = 'n'
	while selection != 'y':
		selection = input('Start poem thread? (y/n)')
		percentage = int(input('How much of the poem to read (%)'))
		if percentage <= 100:
			t = Thread(target=reader)
			t.start()
		else:
			print('Too much poem')

t2 = Thread(target=menu)
t2.start()