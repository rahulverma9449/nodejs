def primeNumber(num):
    if num <= 1:
        return False
    elif num ==2:
        return True
    elif num % 2 == 0:
        return False

    else:
        for i in range(3, int(num**0.5) + 1,2):
            if num % i == 0:
                return False
        return True

for number in range(20,0,-1):
    if primeNumber(number):
        print(number)
