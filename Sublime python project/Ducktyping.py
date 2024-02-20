class PyCharm:

	def execute(self):
		print("Compiling")
		print("Running")
class MyEditor:

	def execute(self):
		print("Spell Check")
		print("data value")
		print("compling")
		print("Spell Check123")

class Laptop:

	def code(self, ide):
		ide.execute()


ide = PyCharm()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)