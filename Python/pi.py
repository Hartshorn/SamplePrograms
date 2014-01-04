# CSCI 1521 Structures
# PI Approximation

# import some needed modules: random to generate random numbers
# and math to do some math

import random
import math

# tell the user what the program will do
# ask for a number using the input() (which returns a string)
# convert this new string to an integer using int()

print("This program will use random numbers to generate an approximation of the value of PI")
print("It will do this using a set number of points input by you")
user_input = input("Please enter a number of points: ")
user_num = int(user_input)

# declare some variables for our count (inside the circle)
# and our total (number of points overall)

count = 0
total = 0

# write a for loop that will assign the values to our points
# (x,y) represents a point on a graph, so we assign values to
# x_val and y_val as random numbers. The for loop will run through
# and make a point for as many times as the user inputs

for i in range(0, user_num):
    x_val = random.uniform(0,2)
    y_val = random.uniform(0,2)
	
# still inside the for loop, we take each generated point and
# run it through our formula to get a value for the distance
# of each point from the center of the circle

    dist = math.sqrt((x_val - 1)**2+(y_val - 1)**2)
	
# because we know this value can not be more than 1 (the radius of
# the circle) we assign the values less than one to count. Afterwards,
# we increment each time though to get a running total. This could done
# with the variable user_num (they should match), but this works as
# a simple double check that everything went smoothly

    if dist < 1 :
        count += 1
    total += 1
	
# now we print out for the user the results. First they get the total
# number of points they input (should match), and then they get the total
# number that were inside the circle

print("\nThese are the results of the PI approximation")
print("Your overall number of points is: %.0f" % total)
print("Your total points inside circle were: %.0f" % count)

# here we calculate our estimate for PI.  We know that the ratio of the area of
# our circle to the area of our square is (PI / 4). So we know that the
# number of points that landed inside the circle divided by the number
# of points overall (count / total) should be the same number. So, doing a
# little rearranging, PI = 4 * (count/total).

est = 4 * (count/total)

# print this value out for the user

print("\nThe estimated value for PI is: %.4f" % est)

# our math module has its own value for PI (a very accurate one), so we can
# compare our estimate with this number to see how close we got

diff = est - math.pi

# and print that out for the user, too

print("The difference between this and the actual value for PI is %.4f" % diff)
