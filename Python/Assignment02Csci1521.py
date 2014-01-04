# CSCI 1521 - Fall 2013
# wed 4:00-6:00p and online

# Student Name: Michael Palmer
# Date complete: Tuesday, September 24th, 2013

# This section is from chapter 1, page 78, question 33

import math

# Get information from the user
print("This program will determine your Quarterback's Passer Rating given the input you provide.\n")

comp_str = input("Enter the number of completions per attempt: ")
comp = float(comp_str)

yards_str = input("Enter the number of yards per attempt: ")
yards = float(yards_str)

touch_str = input("Enter the number of touchdowns per attempt: ")
touch = float(touch_str)

inter_str = input("Enter the number of interceptions per attempt: ")
inter = float(inter_str)

# do some math with these numbers

comp_calc = ((comp * 100) - 30) / 20
yards_calc = (yards - 3) / 4
touch_calc = touch * 20
inter_calc = 2.375 - (inter * 35)

# now use the new calculated variables to get passer rating

passRating = ((comp_calc + yards_calc + touch_calc + inter_calc) / 6) * 100

# tell the user what calculations were made

print("\nThese are the adjusted numbers used in the Passer Rating calculation:\n")

print("The adjusted completions: %.4f" % comp_calc)
print("The adjusted yards: %.4f" % yards_calc)
print("The adjusted touchdowns: %.4f" % touch_calc)
print("The adjusted interceptions: %.4f\n" % inter_calc)

# tell the user what the passer rating is
print("The Passer Rating is: %.4f\n" % passRating)

# The following code is the answer to Problem 23, page 149

# Determine the quality of the QB's season based on the calculated numbers

if(passRating < 85):
	print("The QB had a poor season.")
elif(85 < passRating < 90):
	print("The QB had a mediocre season.")
elif(90 < passRating < 95):
	print("The QB had a good season.")
else :
	print("The QB had a great season.")