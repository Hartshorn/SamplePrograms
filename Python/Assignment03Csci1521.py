# CSCI 1521 - Fall 2013
# wed 4:00-6:00p and online

# Student Name: Michael Palmer
# Date complete: Tuesday, October 8th, 2013

import string

# create a string called vowel to hold all of your vowels
# and an empty string where the user will input a word

vowel = 'aeiou'
userWord = ""

# we put everything in a while loop, which runs on the condition
# that the string userWord is not equal to '.' (the end signal).
# ask the user for input.
# and we work through the word starting at the start
# if the first letter (userWord[0]) is in the string vowel,
# then we know it is a vowel.  We simply print the word
# followed by yay.
# if not, we test the next three letters
# when we find the first vowel, we print the word without the
# first few consonants and attach those letters to the end
# with an ay afterwards

while userWord != '.':
	userWord = input('Enter a single english word (hit \'.\' to end): ')
	for char in userWord[0]:	# check first letter
		if char == '.':
			break;
		elif char in vowel:
			print(userWord + 'yay')
		elif char not in vowel:
			for char in userWord[1]:	# check second letter
				if char not in vowel:
					for char in userWord[2]:	# check third letter
						if char not in vowel:
							print(userWord[3:] + userWord[0:3] + 'ay')	# print the fourth letter to the end, followed by the first three letters plus ay
						else :
							print(userWord[2:] + userWord[0:2] + 'ay')	# print the third letter to the end, followed by the first two letters plus ay
				else :
					print(userWord[1:] + userWord[0] + 'ay')	# print the second letter to the end, followed by the first letter plus ay					
		else :
			print("Invalid entry")
			
# this will not work for "Schtschurowskia", which is the name of a plant
# and starts with seven consonants
# http://www.theplantlist.org/browse/A/Apiaceae/Schtschurowskia/
