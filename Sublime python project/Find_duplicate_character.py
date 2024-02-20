def duplicate_char(string):
	a = set()
	duplicates = set()

	for char in string:
		if char in a:
			duplicates.add(char)
		else:
			a.add(char)
	return list(duplicates)

my_string =  "rahuverma"
result = duplicate_char(my_string)
print(result)
