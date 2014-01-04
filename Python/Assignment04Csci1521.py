

# this program defines a function called progress
# that takes a user input and runs a progress bar
# for the specified length of time. The bar (according
# to the question) is only 10 Xs wide, so the input number
# is divided by 10 to get a number of Xs

import time

# get input from the user

userInput = input('Enter a number of seconds: ')
userInt = int(userInput)


# define the function
# use the time.time() module to get the current time,
# set the time0 variable to the initial time.time()
# and use the change in that time to show elapsed time

def progress(userInt):
	count = userInt / 10
	time0 = time.time()
	endTime = time.time() - time0
	
	while((time.time() - time0) <= userInt):
		if(int(time.time() - time0) != 0):
			if(int(time.time() - time0) % count == 0):
				print('X', end="")
				time.sleep(1.0 - endTime)
	
	print("\n", time.time() - time0, "seconds elapsed")
	print("\n", endTime, " is endTime")
# logic of the while loop:
# while the time elapsed is not equal to the user input
# time, if the time elapsed is not equal to zero and 
# if the elapsed time divided by 10 has no remainder,
# print an X, otherwise don't do anything

# run the function using the user input
progress(userInt)

# I am aware that this program is incomplete, however
# I have run out of time (my own fault).  My problem here
# is the interval on which the X is printed.  Because
# I have turned the interval into an integer, the X prints
# repeatedly for the entire passing second. But when I leave
# the interval as a float, the program won't print any Xs at all.
# This is making me crazy.
