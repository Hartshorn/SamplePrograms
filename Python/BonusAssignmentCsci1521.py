import csv

# define some useful functions
# begin function definition section
def deleteRow(list):
	userChoiceStr = input("Which row would you like to delete: ")
	userChoice = int(userChoiceStr) - 1
	list.remove(list[userChoice])
	
def insertRow(list):
	userChoiceStr = input("After which row would you like to insert a new one: ")
	userChoice = int(userChoiceStr)
	newList = []
	for row in list:
		if(list.index(row) == userChoice):
			newList.append([""])
			newList.append(row)
		else :
			newList.append(row)
	return newList

def insertCol(list):
	userChoiceStr = input("After which column would you like to insert a new one: ")
	userChoice = int(userChoiceStr)
	for row in list:
		for i in row:
			if(row.index(i) == userChoice):
				row.insert(userChoice, "")
				
	
def deleteCol(list):
	userChoiceStr = input("Which column would you like to delete: ")
	userChoice = int(userChoiceStr) - 1
	for i in list:
		i.remove(i[userChoice])

def change(list,row,column,new):
	list[row].remove(list[row][column])
	list[row].insert(column, new)
# end function definition section

# begin main program
# ask user for filename, open it, and save it to a list; this
# will create a list of lists.

userFile = input("Enter the name of a file to open (without .csv): ")
workingFile = open(userFile + ".csv", "r")
reader = csv.reader(workingFile)
holdList = []
for row in reader:
	holdList.append(row)
workingFile.close()

# show the user the current file

print("\nHere is what your file looks like:\n")
for row in holdList:
	print("\t".join(row))
	
# user choice menu

keepGoing = True

while(keepGoing):
	print("\nWhat would you like to do?\n")
	print("Delete information:  d")
	print("Insert blank row or column:  i")
	print("Change entry:  c")
	print("Reprint complete file: r")
	print("Output to new file:  o")
	print("Quit:    q\n")
	userChoice1 = input("Please select an action: ")
	
	# user delete information section
	if(userChoice1 == "d"):
		userChoice = input("Would you like to delete a row, column, or entry (r / c / e): ")
		if(userChoice != "e"):
			userChoice = input("Would you like to delete a row or column: (r or c): ")
			if(userChoice == "r"):
				deleteRow(holdList)
			if(userChoice == "c"):
				deleteCol(holdList)
		if(userChoice == "e"):
			userChoice = input("Which row is the item in: ")
			userRow = int(userChoice) - 1
			userChoice = input("Which column is the item in: ")
			userCol = int(userChoice) - 1
			change(holdList, userRow, userCol, " ")
		else :
			print("Invalid Entry")
	
	# user insert information section
	if(userChoice1 == "i"):
		userChoice = input("Would you like to insert a row or column (r or c): ")
		if(userChoice == "r"):
			holdList = insertRow(holdList)
		if(userChoice == "c"):
			insertCol(holdList)
		elif(userChoice != ("r" | "c")) :
			print("Invalid Entry")
			
	# user change information section
	if(userChoice1 == "c"):
		userChoice = input("Which row is the item in: ")
		userRow = int(userChoice) - 1
		userChoice = input("Which column is the item in: ")
		userCol = int(userChoice) - 1
		userChoice = input("What is the new value: ")
		change(holdList, userRow, userCol, userChoice)
		
	# user reprint file section
	if(userChoice1 == "r"):
		print("\nHere is what your file looks like:\n")
		for row in holdList:
			print("\t".join(row))
			
	# output file section
	if(userChoice1 == "o"):
		userChoice = input("What is the name of the output file: ")
		outFile  = open(userChoice, "w")
		writer = csv.writer(outFile, quoting=csv.QUOTE_ALL)
		writer.writerow(holdList)
	
	# user quit section
	if(userChoice1 == "q"):
		keepGoing = False;
		
		
