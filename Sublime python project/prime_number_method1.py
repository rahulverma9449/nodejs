start = int(input("Enter your number"))
end = int(input("Enter your number"))

for num in range(start, end + 1):
  if num > 1:
    for i in range(3, int(num**0.5) +1,2):
      if (num % i == 0):
        break 
      else:
        print(num)