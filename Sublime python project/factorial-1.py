
## Iterative Approch

def factorial(n):
	result  = 1
	for i in range(1, n+1 ):
		result *= i 

	return result 

def factorial_2(n):
	if n==0:
		return 1
	else:
		return n*factorial_2(n-1)

number = int(input("Enter value"))
result = factorial(number)
result1 = factorial_2(number)
print(result1)
print(result)