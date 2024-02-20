def isvalidParenthesis(expression):
	stack = []
	dict = {")":"(","}": "{", "]": "["}
	for char in expression:
		if char in dict:
			element = stack.pop() if stack else "#"
			if dict[char] != element:
				return False
		else:
			stack.append(char)
	return not stack

input_expression = "{[(){}}"

result = isvalidParenthesis(input_expression)
print(result) 

 