
class Solution:
    def missingNumber(self,array,n):
       
        return ((n)*(n+1)//2)-sum(array)
array = [1, 2, 3, 5, 6]
n = 6
missing_number = Solution().missingNumber(array, n)
print(f"The missing number is: {missing_number}")

      
      
      
    