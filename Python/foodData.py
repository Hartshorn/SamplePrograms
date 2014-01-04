
# import regular expressions module

import re

# this section will define a function with a string as a formal
# parameter. The function creates a search method, which will search
# through a given string. Using this we can test if a user-entered term
# is in any of the food description strings.

def wordFind(word):
    return re.compile(r'\b({})\b'.format(word)).search

# this section will open the data file, extract each line as a
# list of string values, and append each list into one bigger list
# this section will handle all data-stream interactions, and close
# when completed.

holdList = []
fullDataList = []

abbrv = open("ABBREV.txt")
for line in abbrv:
    holdList = line.split(sep='^')
    fullDataList.append(holdList)
abbrv.close()

# test for accuracy: print out random entries(name only)
#print(fullDataList[4][1], fullDataList[76][1], fullDataList[45][1], 
#       fullDataList[34][1], fullDataList[3][1])

# explain the program to the user.

print("This program will ask for individual meal items.")
print("It will enter your items, or give suggestions.")
print("It will then give you nutritional information ")
print("based on what you have entered.\n")

# make a loop to search through possible foods: this loop will look
# at the user entered data. It will search for a possible match,
# returning anything with the user entered string in it.
# While possibly problematic, this method will give the user
# the most options based on the given data set.

mealItems = []

while(len(mealItems) < 3):
    entryError = True
    while(entryError):

        entryList = []
        
        userFirstChoice = input("Please enter a meal item: ")
        userFirstUpper = userFirstChoice.upper()
        
        for list in fullDataList:
            for element in list:
                if(wordFind(userFirstUpper)(element)):
                    entryList.append(list[1])
        
        if(len(entryList) > 200):
            print("Please be more specific")
        elif(200 >= len(entryList) >= 1):
            print("\nYou entered {} - here are your choices:\n".format(userFirstUpper))
            for i in range(0,len(entryList)):
                print(i+1, entryList[i])
            userSecondChoice = input("\nChoose a number:\n")
            userSecondInt = int(userSecondChoice)
            mealItems.append(entryList[userSecondInt-1])
            entryError = False
        else:
            print("ERROR: No foods found!")



# now match the meal items with their respective lines in the
# fullDataList; this will make them easy to pull nutritional
# data from

mealList = []

for list in fullDataList:   # for each list in the fullDataList
    for element in list:        #for each item in the list
        for item in mealItems:      # for each item in mealItems
            if(item == element):    	# if item matches element
                mealList.append(list)       # save the list containing it

# test for accuracy
#print(mealList[0])

# this section will print out relevant data for each food item
# the user has chosen.
# PRINT OUT INDEX: 1, 3, 5 for name, calories, and protein
# add items here based on index number when assigned

# print out the user's meal

print("\nHere is your meal:\n")
for list in mealList:
    print(list[0],list[1])
    
print("\nHere is your Nutritional Information")
print("\nItem Number |   Calories | Protein | Fat")

calCount = 0
proCount = 0
fatCount = 0

for list in mealList:
    for element in list:
        if(element == list[0]):
            print(element,end='\t')
        if(element == list[3]):
            print("\t",element,end='  ')
            calCount += float(element)
        if(element == list[4]):
            print("\t",element,end='  ')
            proCount += float(element)
        if(element == list[5]):
            print("\t",element)
            fatCount += float(element)
            
# finish with a total count of all values

print("\nTotal Calories: {} | Total Protein: {} | Total Fat: {}".format(calCount, 
        round(proCount,2), round(fatCount,2)))
