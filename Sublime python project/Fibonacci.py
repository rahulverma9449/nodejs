## Approch_01

def fabonacci(n):
	fib_series = []
	a,b = 0,1
	for _ in range(n):
		fib_series.append(a)
		a,b = b, a + b
	return fib_series


n = 5
result = fabonacci(n)
print(result)