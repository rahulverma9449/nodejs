def count_char(string):
	count_char = {}

	for char in string:
		if char in count_char:
			count_char[char] += 1
		else:
			count_char[char] = 1
	return count_char

input = "Helloworld"
result = count_char(input)
print(result)