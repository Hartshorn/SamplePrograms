

# question 7, page 512 
# There are three class definitions listed: patient, doctor, and record.
# This program, however, attempts to take the assignment one step further
# and creates a simple hospital database. The user can input and output 
# information about the patients and the doctors (the records have not been
# added at this time). The purpose of this extension of the assignment is
# to show the functionality of classes within python. The grader can disregard
# anything written beyond the assigned class definitions, but is encouraged
# to run the program and have a little fun with it.

# begin patient class definition
class Patient(object):

	# initialization (what to create when creating a new object)
	def __init__(self,first='',last='',id=''):

		self.first_name = first
		self.last_name = last
		self.id = id
		self.sex = 'not set'
		self.height = 'not set'
		self.weight = 'not set'
		self.birthdate = 'not set'
		self.address = 'not set'
		self.phone = 'not set'
		
	# first name getter
	def getFirstName(self):

		return self.first_name
		
	# last name getter
	def getLastName(self):

		return self.last_name
		
	# id getter
	def getID(self):

		return self.id
		
	# first, last, and id setter (called update)
	def update(self,first='', last='', id=''):

		if(first):
			self.first_name = first
		if(last):
			self.last_name = last
		if(id):
			self.id = id
	# gender getter
	
	def setGender(self,sex=''):

		if(sex):
			self.sex = sex
			print('Gender set to: {}'.format(self.sex))
			
		else :
			return 'Gender not set'
			
	# gender setter
	def getGender(self):

		return self.sex
		
	# height setter
	def setHeight(self, height=''):

		if(height):
			self.height = height
			print('Height set to: {}'.format(self.height))
			
		else :
			print('Height not set')
			
	# height setter
	def getHeight(self):

		return self.height
		
	# weight setter
	def setWeight(self, weight=''):

		if(weight):
			self.weight = weight
			print('Weight set to: {}'.format(self.weight))
			
		else :
			print('Weight not set')
			
	# weight getter
	def getWeight(self):

		return self.weight
		
	# birth date setter
	def setBirthdate(self, birthdate=''):

		if(birthdate):
			self.birthdate = birthdate
			print('Birthdate set to: {}'.format(self.birthdate))
			
		else :
			print('Birthdate not set')
			
	# birth date getter
	def getBirthdate(self):

		return self.birthdate
		
	# address setter
	def setAddress(self,address=''):

		if(address):
			self.address = address
			print('Address set to: {}'.format(self.getAddress()))
		else :
			print('Address not set')
		
	# address getter
	def getAddress(self):

		return '{}'.format(self.address)
		
	# phone setter
	def setPhone(self, phone=''):
	
		if(phone):
			self.phone = phone
			print('Phone number set to: {}'.format(self.getPhone()))
		else :
			print('Phone number not set')
			
	# phone setter
	def getPhone(self):
	
		return self.phone
		
	# This loop is a setter method that will run through all of the other setter
	# methods listed above. It is used as a general purpose setter, so that
	# any information that needs to be changed can be done so locally
	def setInfo(self):
	
		loopOut1 = True
	
		while(loopOut1):
		
			print('What info would you like to set?')
			userChoice = input('Name, ID, Gender, Height, Weight, Birthdate, \
			Address, Phone Number (Q to quit)\n').lower()

			if(userChoice == 'name'):
				userNameChoice = input('First or Last name?\n').lower()

				if(userNameChoice == 'first'):
					userName = input('Enter the name to set:\n').lower()
					self.update(userName)
					print('Patient first name set to: {}'.format(self.getFirstName()))

				elif(userNameChoice == 'last'):
					userName = input('Enter the name to set:\n').lower()
					self.update('', userName)
					print('Patient last name set to: {}'.format(self.getLastName()))

				#else :
					#print('Error: Bad Choice')

			if(userChoice == 'id'):
				userChoice = input('Enter new ID #')
				self.update('', '', userChoice)
				print('Patient ID # set to: {}'.format(self.getID()))

			if(userChoice == 'gender'):
				userChoice = input('Enter the gender to set:\n').lower()
				self.setGender(userChoice)

			if(userChoice == 'height'):
				userChoice = input('Enter the height to set:\n').lower()
				self.setHeight(userChoice)

			if(userChoice == 'weight'):
				userChoice = input('Enter the weight to set:\n').lower()
				self.setWeight(userChoice)

			if(userChoice == 'birthdate'):
				userChoice = input('Enter the birthdate to set:\n').lower()
				self.setBirthdate(userChoice)
			
			if(userChoice == 'address'):
				userChoice = input('Enter the address to set: \n').lower()
				self.setAddress(userChoice)
			
			if(userChoice == 'phone number'):
				userChoice = input('Enter the phone number:\n').lower()
				self.setPhone(userChoice)
			
			if(userChoice == 'q'):
				loopOut1 = False
			
			#else :
				#print('Invalid Choice')

	# This loop is a getter method that will loop through all of the other getter
	# methods listed above. It is used as a general purpose getter, allowing
	# for attribute retrieval from a single source
	def getInfo(self):
		
		loopOut2 = True
		
		while(loopOut2):
		
			print('What would you like to know?')
			userChoiceUp = input('Name, ID, Gender, Height, Weight, \
			Birthdate, Address, Phone Number (Q to quit)\n')
			userChoice = userChoiceUp.lower()

			if(userChoice == 'name'):
				print('Patient: {} {}'.format(self.first_name,self.last_name))
				
			if(userChoice == 'id'):
				print('ID #: {}'.format(self.id))
				
			if(userChoice == 'gender'):
				print('Patient Gender: {}'.format(self.getGender()))
				
			if(userChoice == 'height'):
				print('Patient Height: {}'.format(self.getHeight()))
				
			if(userChoice == 'weight'):
				print('Patient Weight: {}'.format(self.getWeight()))
				
			if(userChoice == 'birthdate'):
				print('Patient Birthdate: {}'.format(self.getBirthdate()))
				
			if(userChoice == 'address'):
				print('Patient Address: {}'.format(self.getAddress()))
				
			if(userChoice == 'phone number'):
				print('Patient Phone Number: {}'.format(self.getPhone()))
			
			if(userChoice == 'q'):
				loopOut2 = False

	# printing method, used to print simple patient information
	def __str__(self):
	
		return '{} {}, ID:{}'.format(self.first_name,self.last_name,self.id)
		
# end patient class definition

# begin doctor class definition
class Doctor(object):

	# initialization method
	def __init__(self,first='',last='', id=''):
		self.first_name = first
		self.last_name = last
		self.id = id
		self.qual = 'not set'
		self.phone = 'not set'
		self.spec = 'not set'
		self.office = 'not set'
		self.loc = 'not set'
		
	# first name getter
	def getFirstName(self):
		
		return self.first_name
		
	# last name getter
	def getLastName(self):
		
		return self.last_name
		
	# id getter
	def getID(self):
		
		return self.id
		
	# setter for all three first, last and id (called update)
	def update(self):
		if(first):
			self.first_name = first
		if(last):
			self.last_name = last
		if(id):
			self.id = id
			
	# qualification setter
	def setQual(self, qual=''):
		
		if(qual):
			self.qual = qual
			print('Qualification set to: {}'.format(self.getQual()))
		
		else :
			print('Qualification not set')
			
	# qualification getter
	def getQual(self):
	
		return self.qual
		
	# phone setter
	def setPhone(self, phone=''):
	
		if(phone):
			self.phone = phone
			print('Phone number set to: {}'.format(self.getPhone()))
		else :
			print('Phone number not set')
			
	# phone getter
	def getPhone(self):
	
		return self.phone
		
	# specialization setter
	def setSpec(self, spec=''):
		
		if(spec):
			self.spec = spec
			print('Specialization set to: {}'.format(self.getSpec()))
		else :
			print('Specialization not set')
			
	# specialization getter
	def getSpec(self):
	
		return self.spec
		
	# office hours setter
	def setHours(self, hours=''):
		
		if(hours):
			self.hours = hours
			print('Hours set to: {}'.format(self.getHours()))
		else :
			print('Hours not set')
			
	# office hours getter
	def getHours(self):
	
		return self.hours
		
	# office location setter
	def setLoc(self, loc=''):
	
		if(loc):
			self.loc = loc
			print('Office Location set to: {}'.format(self.getLoc()))
		else :
			print('Office location not set')
			
	# office location getter
	def getLoc(self):
	
		return self.loc
		
	# This loop is a general purpose setter, allowing the setting
	# of any attribute field in the class from one method
	def setInfo(self):
		
		loopOut3 = True
		
		while(loopOut3):
		
			print('What information would you like to enter?')
			userChoiceUp = input('Name, ID, Qualification, Phone Number, \
			Specialization, Office Hours, Office Location (Q to quit)\n')
			userChoice = userChoiceUp.lower()
			
			if(userChoice == 'name'):
				userNameChoiceUp = input('First or Last name?\n')
				userNameChoice = userNameChoiceUp.lower()

				if(userNameChoice == 'first'):
					userNameUp = input('Enter the name to set:\n')
					userName = userNameUp.lower()
					self.update(userName)
					print('Doctor first name set to: {}'.format(self.getFirstName()))

				elif(userNameChoice == 'last'):
					userNameUp = input('Enter the name to set:\n')
					userName = userNameUp.lower()
					self.update('', userName)
					print('Doctor last name set to: {}'.format(self.getLastName()))

				else :
					print('Error: Bad Choice')
					
			if(userChoice == 'id'):
				userChoice = input('Enter new ID #\n')
				self.update('', '', userChoice)
				print('Doctor ID # set to: {}'.format(self.getID()))
					
			if(userChoice == 'qualification'):
				userChoice = input('Enter qualification (M.D. or D.O.):\n')
				self.setQual(userChoice)
			
			if(userChoice == 'specialization'):
				userChoice = input('Enter specialization:\n')
				self.setSpec(userChoice)
				
			if(userChoice == 'phone number'):
				userChoice = input('Enter phone number:\n')
				self.setPhone(userChoice)
			
			if(userChoice == 'office hours'):
				userChoice = input('Enter office hours:\n')
				self.setHours(userChoice)
			
			if(userChoice == 'office location'):
				userChoice = input('Enter office location:\n')
				self.setLoc(userChoice)
			
			if(userChoice == 'q'):
				loopOut3 = False
				
	# This method is a general purpose getter method, allowing
	# for all attribute retrieval from a single method
	def getInfo(self):
		
		loopOut4 = True
		
		while(loopOut4):
		
			print('What information would you like?')
			userChoiceUp = input('Name, ID, Qualification, Phone Number, \
			Specialization, Office Hours, Office Location (Q to quit)\n')
			userChoice = userChoiceUp.lower()
			
			if(userChoice == 'name'):
				print('Doctor Name: {} {}'.format(self.getFirstName(), self.getLastName()))
				
			if(userChoice == 'id'):
				print('Doctor ID #: {}'.format(self.getID()))
				
			if(userChoice == 'qualification'):
				print('Doctor Qualification: {}'.format(self.getQual()))
			
			if(userChoice == 'specialization'):
				print('Doctor Specialization: {}'.format(self.getSpec()))
				
			if(userChoice == 'phone number'):
				print('Doctor Phone Number: {}'.format(self.getPhone()))
			
			if(userChoice == 'office hours'):
				print('Doctor Office Hours: {}'.format(self.getHours()))
			
			if(userChoice == 'office location'):
				print('Doctor Office Location: {}'.format(self.getLoc()))
			
			if(userChoice == 'q'):
				loopOut4 = False
				
	# printing method (defines print() functionality)
	def __str__(self):

		return '{} {}, ID:{}'.format(self.first_name,self.last_name,self.id)
		
# end doctor class definition

# begin record class definition
class Records(object):

	# initialization method
	def __init__(self, patientID='', doctorID='', fileNum=''):
		
		self.patientID = patientID
		self.doctorID = doctorID
		self.fileNum = fileNum
		
	# this does not save the info; each time the method is called it resets the array to empty,
	# but putting them outside the method makes them inaccessible
	def setInfo(self):
		
		healthProb = []
		medications = []
		cost = 0;
	
		print('Please choose record information to enter\n')
		userChoiceUp = input('Health Problems, Medications, Cost, Final Report:\n')
		userChoice = userChoiceUp.lower()
		
		if(userChoice == 'health problems'):
			done1 = True
			while(done1):
				problem = input('Enter Health Problem (q when done): ')
				if(problem == 'q'):
					done1 = False
				else :
					healthProb.append(problem)
				
		if(userChoice == 'medications'):
			done2 = True
			while(done2):
				meds = input('Enter Medications (q when done): ')
				if(meds == 'q'):
					done2 = False
				else :	
					medications.append(meds)
				
		if(userChoice == 'cost'):
			for i in healthProb:
				cost += 1000
			for i in medications:
				cost += 1000
			print('The total cost: ${}'.format(cost))
			
		if(userChoice == 'final report'):
			print('Patient: {}, Doctor: {}, Record #: {}'.format(self.patientID, self.doctorID, self.fileNum))
			print('Health Problems: {}'.format(healthProb))
			print('Medications: {}'.format(medications))
			print('Total Cost: {}'.format(cost))
	# printing method
	def __str__(self):
	
		return 'Patient: {}, Doctor: {}, Record #: {}'.format(self.patientID, self.doctorID, self.fileNum)

# end record class definition

# this section will attempt to mimic an actual hospital
# database. It will ask to enter out receive information
# that is saved.

print('###########################################')
print("Welcome to the Hospital Database")
print("Here you will be able to input or output ")
print("information about patients, doctors, or records.")
print('###########################################')

more = True
patients = []
doctors = []
records = []

while(more):

	answer = input("\nWould you like to input or output information? (q to quit)\n").lower()
	
	if(answer == 'input'):
		answer = input("For a patient or doctor?\n").lower()
		
		if(answer == 'patient'):
			answer = input("New or current?\n").lower()
			
			if(answer == 'new'):
				nameFirst = input("Enter patient's first name: ").lower()
				nameLast = input("Enter patient's last name: ").lower()
				idNum = input("Enter patient's ID number: ").lower()
				
				patient = Patient(nameFirst, nameLast, idNum)
				
				print("\nNew Patient: ", end='')
				print(patient)
				patients.append(patient)
				
				answer = input("Would you like to enter more information? (y or n): ").lower()
				
				if(answer == 'y'):
					patient.setInfo()
					
				if(answer == 'n'):
					continue;
					
			if(answer == 'current'):
				idNum = input("Enter the patient ID number: ")
				
				for i in patients:
					if(idNum == i.getID()):
						i.setInfo()
					else:
						print("Patient not in database")
			#else :
				#print("Error 1: try again")
				
		if(answer == 'doctor'):
			answer = input("New or current?\n").lower()
			
			if(answer == 'new'):
				nameFirst = input("Enter doctor's first name: ").lower()
				nameLast = input("Enter doctor's last name: ").lower()
				idNum = input("Enter doctor's ID number: ").lower()
				
				doctor = Doctor(nameFirst, nameLast, idNum)
				
				print("\nNew Doctor: ", end='')
				print(doctor, '\n')
				doctors.append(doctor)
				
				answer = input("Would you like to enter more information? (y or n): ").lower()
				
				if(answer == 'y'):
					doctor.setInfo()
					
				if(answer == 'n'):
					continue;
					
			if(answer == 'current'):
				idNum = input("Enter the doctor ID number: ")
				
				for i in doctors:
					if(idNum == i.getID()):
						i.setInfo()
					else :
						print("Doctor not in database")
						
		#else :
			#print("Error 2: try again")
			
	if(answer == 'output'):
		answer = input("For a patient or doctor?\n")
		
		if(answer == 'patient'):
			idNum = input("Enter the patient ID number: ")
			
			for i in patients:
				if(idNum == i.getID()):
					i.getInfo()
				else:
					print("Patient not in database")
					
		if(answer == 'doctor'):
			idNum = input("Enter doctor ID number: ")
			
			for i in doctors:
				if(idNum == i.getID()):
					i.getInfo()
				else :
					print("Doctor not in database")
					
		#else :
			#print("Error 3: try again")
			
	if(answer == 'q'):
		more = False
			
			
			
