def findtwolargestnum(arr):
  if len(arr)<2:
    return "Array"
  
  first_max = max(arr[0],arr[1])
  second_max = min(arr[0],arr[1])
  
  for num in arr[2:]:
      if num>first_max:
        second_max = first_max
        first_max = num
      elif num > second_max:
        second_max = num
        
  return first_max, second_max


numbers = [7, 8, 23, 14, 2]
result = findtwolargestnum(numbers)

print(f"The first two largest numbers in the array are: {result}")