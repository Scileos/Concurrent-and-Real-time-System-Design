#ToDo
#Look into cancelling python input


from threading import Thread
from threading import Lock
import threading
import time
from random import randint

Wheels = [0, 0, 0, 0, 0, 0] #Array where each element represents a wheel
wheelIndexes = [] #Array that stores the wheels the user decides to hit with problems
log = [] #Log of solutions tried and is printed at the end of the run 
menuSelection = 0 #Set menuCondition as Menu
complete = False #Initialise finish condition
noOfProblems = 0 #Number of problems <= 5
#Initialise solution flags
tried_DD = False
tried_RW = False
tried_LW = False
roverState = 'vectoring' #Initialize rover state

cv = threading.Condition() #Initialise condition variable

#Function that displays relevant menu choices, called when a menu is needed
def displayMenu():
	print('Rover is vectoring, thow problem at rover?')
	print('1. Small Rock')
	print('2. Sinking')
	print('3. Freewheeling')

#Function that resets the solution_tried markers which are used to determine which solutions have already been attempted
def resetSolutionMarker():
	global tried_DD
	global tried_LW
	global tried_RW
	
	tried_DD = False
	tried_LW = False
	tried_RW = False

#Function that resets the variables/lists used in rover manipulation, basically sends the program back to the start again
def resetRover():
	global menuSelection
	global wheelIndexes
	global affectedWheels
	global roverState

	menuSelection = 0
	wheelIndexes = []
	affectedWheels = []
	roverState = 'vectoring'

	

#Function to randomly select the success of the problem solver -- 80% to succeed
def randomChance():
	Success = False
	i = randint(1,10)
	if i < 8:
		Success = True
	return Success

#Function to select which wheels to throw problems at
def selectWheels():
	global wheelIndexes
	global Wheels
	global menuSelection

	affectedWheels = int(input('How many wheels to affect?'))
	for i in range(0, affectedWheels):
		wheelIndex = (int(input('Wheel index? (1-6)')))
		while wheelIndex not in (1,2,3,4,5,6):
			print('Not in range, valid indexes are 1-6')
			wheelIndex = (int(input('Wheel index? (1-6)')))
		wheelIndexes.append(wheelIndex - 1)
	for i in range(0, len(wheelIndexes)):
		Wheels[wheelIndexes[i]] = menuSelection

#Function that attempts to solve a problem using random chance to determine success
def attemptSolve():
	global wheelIndexes
	global Wheels
	tempWheels = list(Wheels)

	for i in wheelIndexes:
		result = randomChance()
		if result == True:
			tempWheels[i] = 0
			logSuccess = 'Wheel ', i+1 , ' solved'
			log.append(logSuccess)
		else:
			logFail = 'Unable to solve wheel ', i+1
			log.append(logFail)
	if tempWheels == [0,0,0,0,0,0]:
		Wheels = [0,0,0,0,0,0]

#Thread for the different direction solution, exits program if failure, continues if success
def tryDifferentDirection():
	global Wheels
	global tried_DD
	global roverState
	global menuSelection
	global wheelIndexes
	global complete

	while complete != True:
		if roverState == 'stopped' and tried_DD == False:
			cv.acquire()
			log.append('Trying different direction as solution')
			attemptSolve()
			if Wheels != [0,0,0,0,0,0]:
				tried_DD = True
				log.append('Unable to solve with new direction')
				cv.notifyAll()
				cv.release()
				time.sleep(1)
			else:
				for i in range(0,len(wheelIndexes)):
					wheelIndexes[i] = wheelIndexes[i] + 1
				logSuccess = 'Wheels ', str(wheelIndexes) , ' fixed by trying a new direction'
				log.append(logSuccess)
				resetRover()
				cv.notifyAll()
				cv.release()
				time.sleep(1)
	
#Thread for the raise wheel solution, exits program if failure, continues if success
def tryRaiseWheel():
	global Wheels
	global tried_RW
	global roverState
	global tried_DD
	global menuSelection
	global wheelIndexes
	global complete

	while complete != True:
		if roverState == 'stopped' and tried_RW == False and tried_DD == True:
			log.append('Trying raising wheel as solution')
			cv.acquire()
			attemptSolve()
			if Wheels != [0,0,0,0,0,0]:
				tried_RW = True
				log.append('Unable to solve by raising wheels')
				cv.notifyAll()
				cv.release()
				time.sleep(1)
			else:
				for i in range(0,len(wheelIndexes)):
					wheelIndexes[i] = wheelIndexes[i] + 1
				logSuccess = 'Wheels ', str(wheelIndexes) , ' fixed by raising wheels'
				log.append(logSuccess)
				resetRover()
				cv.notifyAll()
				cv.release()
				time.sleep(1)

#Thread for the lower wheel solution,  exits program if failure, continues if success	
def tryLowerWheel():
	global Wheels
	global tried_LW
	global roverState
	global tried_RW
	global menuSelection
	global wheelIndexes
	global complete

	while complete != True:
		if roverState == 'stopped' and tried_LW == False and tried_RW == True:
			log.append('Trying lowering wheel as solution')
			cv.acquire()
			attemptSolve()
			if Wheels != [0,0,0,0,0,0]:
				tried_LW = True
				log.append('Unable to solve by raising wheels')
				cv.notifyAll()
				cv.release()
				time.sleep(1)
			else:
				for i in range(0,len(wheelIndexes)):
					wheelIndexes[i] = wheelIndexes[i] + 1
				logSuccess = 'Wheels ', str(wheelIndexes) , ' fixed by lowering wheels'
				log.append(logSuccess)
				resetRover()
				cv.notifyAll()
				cv.release()
				time.sleep(1)

#Thread used to determine when all solutions have failed
def solutionsFailed():
	global tried_DD
	global tried_RW
	global tried_LW
	global roverState
	global complete

	while complete != True:
		if tried_DD == True and tried_RW == True and tried_LW == True and roverState == 'stopped':
			cv.acquire()
			log.append('Unable to solve problem automatically, Calling for assistance')
			resetRover()
			cv.notifyAll()
			cv.release()
			time.sleep(1)
		

#Thread to throw rock problem
def singleRock():
	global menuSelection
	global Wheels
	global roverState
	global noOfProblems
	global complete

	while complete != True:
		if menuSelection == 1 and roverState == 'vectoring':
			cv.acquire()
			noOfProblems += 1
			if noOfProblems > 5:
				complete = True
				cv.notifyAll()
				cv.release()
				time.sleep(1)
			else:
				logProblem = 'Problem ', noOfProblems , ' SINGLE ROCK'
				log.append('')
				log.append(logProblem)
				selectWheels()
				print('Attempting to solve problems')

				roverState = 'stopped'
				menuSelection = None

				cv.notifyAll()
				cv.release()
				time.sleep(1)

#Thread to throw sinking wheel problem
def sinkingWheel():
	global menuSelection
	global Wheels
	global roverState
	global noOfProblems
	global complete

	while complete != True:
		if menuSelection == 2 and roverState == 'vectoring':
			cv.acquire()
			noOfProblems += 1
			if noOfProblems > 5:
				complete = True
				cv.notifyAll()
				cv.release()
				time.sleep(1)
			else:
				logProblem = 'Problem ', noOfProblems , ' SINKING WHEEL'
				log.append('')
				log.append(logProblem)
				selectWheels()
				print('Attempting to solve problems')

				roverState = 'stopped'
				menuSelection = None

				cv.notifyAll()
				cv.release()
				time.sleep(1)

#Thread to throw freewheeling problem
def freeWheeling():
	global menuSelection
	global Wheels
	global roverState
	global noOfProblems
	global complete

	while complete != True:
		if menuSelection == 3 and roverState == 'vectoring':
			cv.acquire()
			noOfProblems += 1
			if noOfProblems > 5:
				complete = True
				cv.notifyAll()
				cv.release()
				time.sleep(1)
			else:
				logProblem = 'Problem ', noOfProblems , ' FREE WHEELING'
				log.append('')
				log.append(logProblem)
				selectWheels()
				print('Attempting to solve problems')

				roverState = 'stopped'
				menuSelection = None

				cv.notifyAll()
				cv.release()
				time.sleep(1)
	
#Thread to display menu and take input problems
def menuCondition():
	global menuSelection
	global Wheels
	global complete
	global roverState
	
	
	while complete != True:
			if menuSelection == 0 and roverState == 'vectoring':
				cv.acquire()
				resetSolutionMarker()
				displayMenu()
				menuSelection = int(input())
				while menuSelection not in (1,2,3):
					menuSelection = int(input('Invalid selection, please try again: '))
				cv.notifyAll()
				cv.release()
				time.sleep(1)
	print('Successful run with the following steps: ')
	for i in log:
		print(i)
	



#Defining threads
singleRock = Thread(target=singleRock)
sinkingWheel = Thread(target=sinkingWheel)
freeWheeling = Thread(target=freeWheeling)
tryDifferentDirection = Thread(target=tryDifferentDirection)
tryRaiseWheel = Thread(target=tryRaiseWheel)
tryLowerWheel = Thread(target=tryLowerWheel)
solutionsFailed = Thread(target=solutionsFailed)
menuCondition = Thread(target=menuCondition)

#Starting threads
singleRock.start()
sinkingWheel.start()
freeWheeling.start()
tryDifferentDirection.start()
tryRaiseWheel.start()
tryLowerWheel.start()
solutionsFailed.start()
menuCondition.start()

