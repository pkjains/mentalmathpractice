import random
#import pandas as pd
import time
#from datetime import datetime, timedelta

#print(datetime.datetime.now())
#now=datetime.now()
#year=now.strftime("%Y")
#print("Year:",year)
#month=now.strftime("%m")
#print("Month:",month)
#day=now.strftime("%d")
#print("Day:",day)
#time=now.strftime("%H:%M:%S")
#print("Time:",time)
#date_time=now.strftime("%Y-%m-%d %H:%M:%S")
#print("date and time:",date_time)
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

#username = input("Enter your first name: ")
while True:
	try:
		username = input("Enter your first name:")
		break
	except ValueError:
		print("That was not a valid name. Try Again")
print("This is mental math challenge for ", username, " on ", now)
score = 0

difficulty = 0
debug = 0

test = 0
if (test==1):
	numProblems=5
	print("\n\n 			TEST MODE IS ON\n\n")
else:
	numProblems = 20


start_time = time.time()
#new_df = pd.read_csv('mentalmathscore.csv')
random.seed(int(start_time))

for i in range(numProblems):
	sign = ""
	answer = 0
	if (difficulty == 0):
		numOne = random.randint(1,100)
		pickOperator = random.randint(1,13)
	elif (difficulty == 1):
		numOne = random.randint(1,1000)
		pickOperator = random.randint(1,13)
	elif (difficulty == 2):
		numOne = random.randint(1,10000)
		pickOperator = random.randint(1,13)

	numTwo = random.randint(1,100)
	
	if (pickOperator == 8):
		pickOperator = 4
		
	if pickOperator in [1,10,11]:
		sign = " + "
		answer = numOne + numTwo
	elif pickOperator in [2,12,13]:
		sign = " - "
		if numOne < numTwo:
			numOne, numTwo = numTwo, numOne
		answer = numOne - numTwo
	elif pickOperator == 3:
		sign = " * "
		numTwo = random.randint(1,10)
		#if numTwo:
		#	numOne, numTwo = numTwo, numOne
		answer = numOne * numTwo
	elif pickOperator == 4:
		sign = " / "
		numTwo = random.randint(1,10)
		if numOne < numTwo:
			numOne, numTwo = numTwo, numOne
		numOne -= (numOne%numTwo)
		answer = numOne / numTwo
	elif pickOperator == 5:
		sign = " + "
		floatOne = round(random.random(),2)
		floatTwo = round(random.random(),2)
		answer = floatOne + floatTwo
	elif pickOperator == 6:
		sign = " - "
		floatOne = round(random.random(),2)
		floatTwo = round(random.random(),2)
		if floatOne < floatTwo:
			floatOne, floatTwo = floatTwo, floatOne
		answer = floatOne - floatTwo
	elif pickOperator == 7:
		sign = " * "
		floatOne = round(random.random(),2)
		numTwo = random.randint(1,10)
		numTwo -= numTwo %2
		#if numTwo:
		#	numOne, numTwo = numTwo, numOne
		answer = round(floatOne * numTwo,2)
	elif pickOperator == 8:
		sign = " / "
		floatOne = random.randint(1,100)
		floatOne -= floatOne%2
		numTwo = random.randint(1,10)
		numTwo -= numTwo %2
		while (floatOne%numTwo != 0):
			floatOne+=1
		#if numTwo:
		#	numOne, numTwo = numTwo, numOne
		answer = floatOne / numTwo
	elif pickOperator == 9:
		sign = " / "
		answer = numTwo - numOne
	elif pickOperator == 6:
		floatOne = round(random.random(),2)
		floatTwo = round(random.random(),2)
		answer = floatOne + floatTwo
	else:
		print ("An error has occured")

	if (pickOperator <=4):
		question = "What is " + str(numOne) + sign + str(numTwo) + "? "
	elif (pickOperator in [5,6]):
		question = "What is " + str(floatOne) + sign + str(floatTwo) + "? "
	elif (pickOperator in [7,8]):
		question = "What is " + str(floatOne) + sign + str(numTwo) + "? "
	elif (pickOperator == 9):
		question = "What is x + " + str(numOne) + " = " + str(numTwo) + "? "
	elif (pickOperator == 10):
		question = "What is " + str(numOne) + sign + "_____ = " + str(answer) + "? "
	elif (pickOperator == 11):
		question = "What is _____ " + sign + str(numOne) + " = " + str(answer) + "? "
	elif (pickOperator == 12):
		question = "What is " + str(numOne) + sign + "_____ = " + str(answer) + "? "
	elif (pickOperator == 13):
		question = "What is _____ " + sign + str(numTwo) + " = " + str(answer) + "? "
	
	while True:
		try:
			if (pickOperator in [5,6,7,8]):
				user_answer = (input(question))
			else:
				user_answer = int(input(question))
			break
		except ValueError:
			print("That was not a valid number. Try Again")

	if (debug == 1):
		print(type(user_answer))
		print(type(answer))
		print("\n\nuser_answer is ", user_answer)
		print ("\n\nCalculated answer is ", answer)
		print("\n\n")

	if (pickOperator in [5,6,7,8]):
		if user_answer == str(round(answer,2)):
			print ("That was the correct answer!")
			score = score + 1
		else:
			print ("That answer was incorrect! The correct answer is ", answer)
	elif (pickOperator in [10,11,12]):
		if user_answer == numTwo:
			print ("That was the correct answer!")
			score = score + 1
		else:
			print ("That answer was incorrect! The correct answer is ", numTwo)
	elif (pickOperator == 13):
		if user_answer == numOne:
			print ("That was the correct answer!")
			score = score + 1
		else:
			print ("That answer was incorrect! The correct answer is ", numOne)
	else:
		if user_answer == answer:
			print ("That was the correct answer!")
			score = score + 1
		else:
			print ("That answer was incorrect! The correct answer is ", answer)

stop_time = time.time()
duration = stop_time - start_time

print ("\n\n", username + " you got " + str(score) + " out of ",numProblems)
print(f'\nTime take for {numProblems} is  {int((time.time() - start_time)/60):0.0f} minutes {((time.time() - start_time)%60):.0f} seconds') # print the time elapsed
