# Inheritance

class A:

	def __init__(self):
		print("In A init")

	def feature1(self):
		print('Feature 1 working')

	def feature2(self):
		print("Features 2  working")

class B:
	def __init__(self):
		# super().__init__()  ## constructor and super class
		print("in B Init")


	def feature3(self):
		print('Feature 3 working')

	def feature4(self):
		print("Features 4  working")

class C(A,B):
	
	def __init__(self):
		super().__init__()
		print('Feature C working')

	def body(self):
		super().feature3()


a1 = C()
a1.feature1()
a1.body()
 

