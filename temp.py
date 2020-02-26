
class Employee:

	def __init__(self, name, yearOfExperience, pastEmployers):

		self.name = name
		self.yearOfExperience = yearOfExperience
		self.pastEmployers = pastEmployers

	#Getter Methods
	def getName(self):
		return self.name

	def getYearOfExperience(self):
		return self.yearOfExperience

	def getPastEmployers(self):
		return self.pastEmployers

	#Setter Methods
	def setName(self, newName):
		self.name = newName

	def setYearOfExperience(self, newYearOfExperience):
		self.yearOfExperience = newYearOfExperience

	def setPastEmployer(self, newEmployer):
		self.pastEmployers.append(newEmployer)

	#Promotion Method
	def needPromotion(self):

		if(yearOfExperience > 5):
			return True
		else:
			return False


class CEO(Employee):
	def __init__(self, name, yearOfExperience, pastEmployers, onForbes, worksForFortune500):
		super().__init__(name, yearOfExperience, pastEmployers)
		self.onForbes = onForbes
		self.worksForFortune500 = worksForFortune500

	def needPromotionMethod(self):
		return False


def main():

	pass

if __name__ == '__main__':
	main()