# prev2 = 0
# prev1 = 1

# print(prev2)
# print(prev1)
# for fibo in range(18):
#   newFibo = prev1 + prev2
#   print(newFibo)
#   prev2 = prev1
#   prev1 = newFibo
  
  
# Implementation Using Recursion

# print(0)
# print(1)
# count =2
# def fibonacci(prev1, prev2):
#   global count
#   if count <=19:
#     newFibo = prev1 + prev2
#     print(newFibo)
#     prev2 = prev1
#     prev1 = newFibo
#     count += 1
#     fibonacci(prev1, prev2)
#   else:
#     return 
# fibonacci(1, 0)



# Method 3

def f(n):
  if n <=1:
    return n
  else:
    return f(n-1) + f(n-2)
  
for i in range(1,10):
  fact = f(i)
  print("fabonacci", fact)