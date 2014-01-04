import random
import turtle

# begin function definition section

# begin rain prediction function
def rainPredict(n):

    rain = 0

    if(1.0 >= n >= 0.98):
        rain = 2
    elif(0.98 > n >= 0.92):
        rain = 1.5
    elif(0.92 > n >= 0.86):
        rain = 1
    elif(0.86 > n >= 0.78):
        rain = 0.75
    elif(0.78 > n >= 0.71):
        rain = 0.25
    else:
        rain = 0

    return rain
# end rain prediction function

# begin century prediction function
def centRain():
	count = 0
	centCount = 0
	rain1 = []
	centRain = []

# this is a while loop inside a while loop. The inside loop
# is the same as the one used to generate a list
# for the growing season. This means that we are making
# a list full of lists, and it is big.

	while(centCount <= 99):
		while(count <= 107):
			rand = random.uniform(0.0,1.0)
			rain1.append(rainPredict(rand))
			count += 1
		centRain.append(rain1)
		centCount += 1
		count = 0
		rain1 = []
	return centRain
# end century prediction function

# the following functions are related to the turtle graphics

# begin word printing function
def turtleWords(list1,list2):                  # this function will write the total and average rainfall
    jack.up()                       # on the graph
    jack.goto(-335,260)
    jack.write("Growing Season", font=(20))
    jack.goto(-320,240)
    jack.write("108 Days", font=(12))
    jack.goto(-335,220)
    jack.write("Total Rainfall", font=(16))
    jack.goto(-320,200)
    jack.write(list1, font=(12))
    jack.goto(-335,180)
    jack.write("Average Daily Rainfall", font=(16))
    jack.goto(-320,160)
    jack.write(list2, font=(12))
# end word printing function

# begin average line generation function
def avgLine(list):
    jack.up()
    jack.goto(-500,-560)  # -260
    jack.setheading(90)
    jack.color("green")
    jack.fillcolor("green")
    jack.down()
    jack.begin_fill()
    jack.forward(300)
    jack.forward(list*100)       # rainAverage times 100 to match rainMult values
    jack.setheading(0)
    jack.forward(1000)
    jack.right(90)
    jack.forward(list*100)       # move forward to the start (108 + 108*2 + 108*3)
    jack.forward(300)
    jack.end_fill()
# end average line generation function

# begin graph line generation function
def graphLines():                   # this function will make graph lines
    jack.goto(-335,-260)
    jack.setheading(90)
    jack.up()
    jack.color("black")
    for i in range(0,200):          # this loop will make a line along the left side
        if(i%10 == 0):              # writing the numbers that are multiples of 10
            jack.write(i/100)       # dividing them by 100 to show 0 to 2 inches.
        jack.forward(1)
    jack.up()
    jack.goto(-300,-280)
    jack.right(90)
    for i in range(0,540):          # this loop will make a line along the bottom
        if(i%100 == 0):             # representing each day in the season (by 10's)
            jack.write(int(i/10)*2)
        jack.forward(1)
# end graph line generation function

# begin bar graph generation function
def barGraph(list):                 	# this function will run for each value in rainMult
    jack.goto(-300,-260)        	# and it will make a simple bar graph
    jack.down()
    jack.left(90)
    for i in list:
        jack.color("green")
        jack.fillcolor("green")
        jack.begin_fill()
        jack.forward(i)
        jack.right(90)
        jack.forward(2)
        jack.right(90)
        jack.forward(i)
        jack.end_fill()
        jack.left(90)
        jack.forward(3)
        jack.left(90)  
# end bar graph generation function

# begin sun function
def makeSun(list):                  	# this function will make a sun in
    jack.up()                   	# in the sky. The rays of sunlight
    jack.goto(200,200)          	# will be made by the values in 
    jack.down()                 	# the rain list
    jack.color("yellow")
    jack.fillcolor("yellow")
    jack.begin_fill()
    for i in list:
        jack.pensize(2)
        n = 0
        while(n <= 2):
            if(i == 0):
                jack.forward(1)
                jack.left(1)
            else:
                jack.right(90)
                jack.forward(i)
                jack.backward(i)
                jack.left(90)
                jack.forward(1)
                jack.left(1)
            n += 1
    for i in range(20):
        jack.forward(1)
        jack.left(1)
    jack.end_fill()
# end sun function

# begin thunderstorm function
def thunderstorm(list):                 # this function will create a thunderstorm on
    jack.color("light grey")        # on the screen. First the clouds will roll in,
    jack.fillcolor("grey")        	# and then the rain will come along with 
    jack.up()                       # dramatic lightning. The rain will fall based
    jack.begin_fill()               # on the amounts in the rain list, mirroring
    jack.goto(-335,155)             # the bar graph below.
    jack.down()
    jack.goto(-335,140)
    jack.setheading(0)
    jack.right(45)
    n = 0
    while(n < 8):
        for i in range(90):
            jack.forward(1)
            jack.left(1)
        jack.right(90)
        n += 1
    jack.setheading(90)
    jack.forward(15)
    jack.end_fill()
    jack.up()
    jack.color("blue")
    jack.goto(-300,120)
    jack.setheading(0)
    for i in list:
        if(i == 0):
            jack.forward(5)
        else:
            jack.right(90)
            jack.down()
            window.bgcolor("white")     # simulated lightning
            jack.forward(i)
            window.bgcolor("light blue")
            jack.backward(i)
            jack.up()
            jack.left(90)
            jack.forward(5)
# end thunderstorm function

# end function definition section

# begin program

# call on the rain prediction function to generate a list
# run a loop for 108 days and save all the values

rain = []
count = 0
newList = []

while(count <= 107):
    rand = random.uniform(0.0,1.0)
    rain.append(rainPredict(rand))
    count += 1

# generate the total rainfall amount, calculate the average using this number

totalRain = sum(rain)
rainAverage = round(totalRain/108,4)

# now we work with our list!
# declare some global variables

noRain = 0
stretch = []
yesRain = 0
maxRain = 0
rainStretch = []
maxStretch = []
lotsOfRain = 0

# the first loop will look at each value in the rain list (each day
# of the season) and increment a counter if it finds a no rain day,
# resetting if it finds a rain day. Each time noRain is incremented, 
# the value is added to the stretch list. We then return the max value
# from stretch (max(stretch)) and print it out. This will return the longest
# stretch of days without rain. The second and third loops do similar actions

for i in rain:
    if(i == 0):
        noRain += 1
        stretch.append(noRain)
    else:
        noRain = 0

for i in rain:
    if(i != 0):
        yesRain += 1
        maxRain += i
        rainStretch.append(yesRain)
        maxStretch.append(maxRain)
    else:
        yesRain = 0
        maxRain = 0

for i in rain:
    if(i >= 1.5):
        lotsOfRain += 1

# print out all of the results

#print("This list represents each day of the growing season")
#print(rain, "\n")
print("ONE YEAR OF GROWING!")
print("Most Dry Days In A Row:", max(stretch))
    
# decide if there was a drought
if(max(stretch) >= 12):
    print("We had a drought!")
else:
    print("No drought this year.")
        
print("Most Rainy Days In A Row:", max(rainStretch))
    
# decide if there was a flood
if((max(rainStretch) >= 5) & (max(maxStretch) >= 6)):
    print("We had a flood this year!")
else:
    print("No flood this year.")
        
print("Days of Rain Above 1.5 Inches:", lotsOfRain, "\n")

print("TOTAL RAINFALL")
print(totalRain)

print("AVERAGE DAILY RAINFALL")
print(rainAverage)


# this section will look at data generated for 100 years
# first we call on our function to generate the data

centRain = centRain()

# declare some new variables to hold the new values

centCount = 0
centTotalRain = 0
centNoRain = 0
centStretch = []
centFullStretch = []
centDrought = 0
centTotalRainList = []
centYesRain = 0
centMaxRain = 0
centRainStretch = []		
centMaxStretch = []
centRainFullStretch = []
centRainMaxStretch = []
centFloodCount = 0

# here we want to look at the values inside of our newly generated list
# but because the values inside are also lists, we have to look at each
# of them as well. We can then add them all together which will give us
# a total rainfall over then 100 years, and then calculate the yearly
# and daily rainfall averages.

for i in centRain:
	for n in i:
		centTotalRain += n
	centTotalRainList.append(centTotalRain)
	centTotalRain = 0
	
for i in centRain:
	for n in i:
		if(n == 0):
			centNoRain += 1
			centStretch.append(centNoRain)
		else:
			centNoRain = 0
	centFullStretch.append(centStretch)
	centStretch = []

for i in centFullStretch:
	if(max(i) >= 12):
		centDrought += 1

for i in centRain:
	for n in i:
		if(n != 0):
			centYesRain += 1
			centMaxRain += n
			centRainStretch.append(yesRain)		# these are lists from each year
			centMaxStretch.append(maxRain)
		else:
			centYesRain = 0
			centMaxRain = 0
	centRainFullStretch.append(centRainStretch)	# these are all 100 years together
	centRainMaxStretch.append(centMaxStretch)
	centRainStretch = []
	centMaxStretch = []


if((max(i)in centRainFullStretch >= 5) & (max(i) in centRainMaxStretch >= 6)):
	centFloodCount += 1

centAvYear = round((sum(centTotalRainList)/100),4)
centAvDay = round(centAvYear/108,4)

# print out our results

print("\nCELEBRATING 100 YEARS OF GROWING!")
print("Average Yearly Inches:", centAvYear)
print("Average Daily Inches:", centAvDay)
print("Years with a drought:", centDrought)
print("Years with a flood:", centFloodCount)
# this is the turtle graphics setup section
# here the window and the turtle will be created

rainMult = [i*100 for i in rain]    # multiply the rain list by 100 to make the values more visible
centTotalRainListMult = [i*10 for i in centTotalRainList] 

window = turtle.Screen()
window.bgcolor("light blue")
window.title("Daily Rainfall Over 108 Days")
jack = turtle.Turtle()
jack.shape("blank")
jack.speed(0)
jack.fillcolor("black")

# now we run all of our turtle related functions
# to make a full picture. Each function uses values
# generated by other functions. Commenting out individual
# functions will alter the overall picture

turtleWords(totalRain,rainAverage)	# write the words
avgLine(rainAverage)				# make the green ground (height is average rainfall line)
graphLines()						# make the x and y axis values
barGraph(rainMult)					# grow the grass (daily rainfall values)
#barGraph(centTotalRainListMult)	# uncomment to see century graph
makeSun(rainMult)					# make sun (rays are daily rainfall values)
thunderstorm(rainMult)				# thunderstorm rolls in (raindrops are daily rainfall values)
