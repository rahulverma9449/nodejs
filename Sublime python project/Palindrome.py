s = input("Enter a string to check: ")
r=s[::-1]
if (r==s):
    print("\n")
    print ("The given string is palindrome.")
else:
    print("Not palindrome")









# def is_palindrome(anjali):
#     anjali = ''.join(filter(str.isalnum, anjali)).lower()
#     return anjali == anjali[::-1]

# input_string =input("Enter value:  ")
# result = is_palindrome(input_string)
# if result:
#     print(f"'{input_string}' is a plandrome")
# else:
#     print(f"'{input_string}' is not plandrome")
    
    
# class Solution:
#     def Palindrome(self, s):
#         if s == s[::-1]:
#             return s
             
#         left = self.Palindrome(s[1:])
#         right = self.Palindrome(s[:-1])
        
#         if len(left) > len(right):
#             return left
#         else:
#             return right
        
        
# solution_instance = Solution()

# # Input String
# input_string = "babad"

# # Output
# result = solution_instance.Palindrome(input_string)
# print(f"Input String: {input_string}")
# print(f"Longest Palindrome: {result}")            
            