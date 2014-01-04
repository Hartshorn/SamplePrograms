# CSCI 1521 - Fall 2013
# wed 4:00-6:00p and online

# Student Name: Michael Palmer
# Date complete: Tuesday, December 3rd, 2013


class Sentence(object):

	def __init__(self, string=''):
	
		self.string = string
		self.stringList = self.string.split()
		
	def get_first_word(self):
		
		return self.stringList[0]
	
	def get_all_words(self):
		
		for i in self.stringList:
			print(i, end=' ')
			
	def replace(self, index, new_word):

		self.stringList[index] = new_word
		
		for i in self.stringList:
			print(i, end=' ')

	def __str__(self):
	
		return '{}'.format(self.string)