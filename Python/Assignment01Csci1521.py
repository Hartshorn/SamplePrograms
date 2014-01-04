# CSCI 1521 - Fall 2013
# wed 4:00-6:00p and online

# Student Name: Michael Palmer
# Date complete: Monday, September 9th, 2013

# Please code your answers below.
  
import math

# get information from the user
gallons_str = input("Enter number of gallons as a decimal number: ")
gallons_float = float(gallons_str)

# convert to liters (1 gal = 3.78541 liters)
liters_float = gallons_float * 3.78541

# calculate number of barrels of oil needed (1 barrel of oil = 19.5 gal)
barrelsOil = gallons_float / 19.5

# calculate the number of pounds of CO2 produced
# 1 gallon produces 20 pounds of CO2
poundsCO2 = gallons_float * 20

# calculate the equivalent energy amount of ethanol gallons
# 1 gallon of gasoline = 115000 BTU of energy
# 1 gallon of ethanol = 75700 BTU of energy
energyGas = gallons_float * 115000
energyEth = gallons_float * 75700

# calculate the price in US dollars
priceUS = gallons_float * 3

# now print out all of the calculated values
print "The number of gallons you entered was %.2f" % gallons_float, "gallons."

print "That number in liters is %.2f" % liters_float, "liters."

print "The number of barrels of oil required to \
make this amount of gasoline is %.2f" % barrelsOil, "barrels."

print "The number of pounds of CO2 produced is %.2f" % poundsCO2, "lbs."

print "The amount of energy contained in this amount \
of gas is %.2f" % energyGas, "BTUs."

print "The amount of energy contained in this same amount \
of ethanol is %.2f" % energyEth, "BTUs."

print "The price of this amount of gas in US dollars is $%.2f." % priceUS


# prompt the user for the number of miles driven per day on average
averageMiles_str = input("How many miles do you drive per day on average: ")
averageMiles_int = int(averageMiles_str)

# calculate the number of gallons used per day, per week, and per month on average
# assuming the average car gets 24.7 mpg
averageGal = averageMiles_int / 24.7
galPerWeek = averageGal * 7
galPerMonth = galPerWeek * 4

# tell them how many gallons they use per day, per week, per month
print "You use %.2f" % averageGal, "gallons per day."
print "You use %.2f" % galPerWeek, "gallons per week."
print "You use %.2f" % galPerMonth, "gallons per month."

# decide whether they use more gallons per day than average
# the average person uses 2.8 gallons per day

if (averageGal > 2.8):
	print "This is %.2f" % (averageGal - 2.8), "gallons more than average."
elif (averageGal == 2.8):
	print "You use the average number of gallons per day."
else:
	print "This is %.2f" % (2.8 - averageGal), "gallons less than average."
