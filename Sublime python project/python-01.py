### Inner class 

class Student:

	def __init__(self, name, rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop()

	def show(self):
		print(self.name, self.rollno)

	class Laptop:  #Inner class

		def __init__(self):
			self.brand = 'HP'
			self.cpu = 'i5'
			self.ram = 8


s1 = Student('rahul', 48)
s2 = Student('john',23)

s1.show()

lap1 =s1.lap
lap2 = s2.lap


print(id(lap1))
print(id(lap2))
















## types of Method

# class Student:

# 	school = 'Telusko'

# 	def __init__(self, m1,m2,m3):
# 		self.m1 = m1
# 		self.m2 = m2
# 		self.m3 = m3

# 	def avr(self):
# 		return (self.m1 + self.m2 + self.m3) / 3

### class method

	# def get_m1(self):
	# 	return self.m1

	# def set_m1(self, value):
	# 	self.m1 = value

### Instance method 
# 	@classmethod  # decorator 
# 	def getschool(cls):
# 		return cls.school

# 	@staticmethod
# 	def info():
# 		print('This is Student class.. in abc module')

# s1 = Student(47, 50,21)
# s2 = Student(89,32,14)

# print(s2.avr())
# print(Student.getschool())

# Student.info()




# class car:   

# 	wheels = 4

# 	def __init__(self):
# 		self.mil = 10
# 		self.com = "BMW"
# c1 = car()
# c2 = car()

# c1.mil = 8
# c2.com = "audi"

# car.wheels = 6

# print(c1.com, c1.mil, c1.wheels)
# print(c2.com, c2.mil, c2.wheels)







# class Computer:
#  	def __init__(self):
#  		self.name = "rahul"
#  		self.age = 28

#  	def compare(self, other):
#  		if self.age == other.age:
#  			return True
#  		else:
#  			return False

# c1 = Computer()
# c1.age = 30
# c2 = Computer()

# if c1.compare(c2):
# 	print('they are same')
# else:
# 	print("They are different")

# print(c1.name)
# print(c2.name)





















# class computer:
# 	def __init__(self, cpu, ram):
# 		self.cpu = cpu 
# 		self.ram = ram

# 	def config(self):
# 		print('Config is ', self.cpu, self.ram)
# comp1 = computer('i5', 17)
# comp2 = computer('rahul', 98)

# comp1.config()
# comp2.config()