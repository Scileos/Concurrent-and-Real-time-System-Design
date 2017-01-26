from threading import Thread
import time

def printer(i):
		time.sleep(5)
		print(i)


t = Thread(target=printer, args=(1,))
t2 = Thread(target=printer, args=(2,))
t3 = Thread(target=printer, args=(3,))
t.start()
t2.start()
t3.start()
