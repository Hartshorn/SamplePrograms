# CSCI 1521 - Fall 2013
# wed 4:00-6:00p and online

# Student Name: Michael Palmer
# Date complete: Tuesday, November 19th, 2013


# encryption function definition start
# this function will take as formal parameters a string
# and an integer. The function will then shift the letters
# of the string by the integer provided
def encrypt(string, int):
        # set some variables, including one
        # that splits the string into individual
        # indexes of a list
        newString = list(string)
        newList = []
        encryptList = []
        # look at each index of the created list
        # if there is a space, simply append the ASCII
        # value to a new list; otherwise shift the value
        # by the factor indicated, then append it
        for i in newString:
			if(ord(i) == 32):
				newList.append(ord(i))
			else:
				newList.append(ord(i) + int)
        # now convert the ASCII values to their associated
        # characters and append this to the final list
        for i in newList:
                encryptList.append(chr(i))
        # the function returns the list of the encrypted string
        return encryptList
# encryption function definition end

# decryption function definition start
# given an encrypted string and a key, this function will
# decrypt the string
def decrypt(string, int):
        # set some variables, split the string into a list
        newString = list(string)
        newList = []
        decryptList = []
        # for each value in the string, append the spaces,
        # shift the characters backwards and append them also
        for i in newString:
			if(ord(i) == 32):
				newList.append(ord(i))
			else:
				newList.append(ord(i) - int)
        # convert and append the ASCII values
        for i in newList:
            decryptList.append(chr(i))
        # return the new decrypted list of characters
        return decryptList
# decryption function definition end

# begin main program

# get some information from the user
userStr = input("Enter a string: ")
userIntStr = input("Enter an encryption shift: ")
userInt = int(userIntStr)

# this loop will ask the user which function to use
# it will then either encrypt their string, or decrypt it

error = True
while(error):
	answer = input("Would you like to encrypt or decrypt this string?\nEnter e or d: ")
	if(answer == "e"):
		newString = encrypt(userStr, userInt)
		error = False
		print("The encrypted string is: ")
		for i in newString:
			print(i,end='')
	elif(answer == "d"):
		oldString = decrypt(userStr, userInt)
		error = False
		print("The decrypted string is: ")
		for i in oldString:
			print(i,end='')
	else:
		print("Error: Invalid Choice!")
		continue;
# end main program
