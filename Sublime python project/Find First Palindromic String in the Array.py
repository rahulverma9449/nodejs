from typing import List
class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""  
input_words = ["abc", "car", "ada", "racecar", "cool"]


solution_instance = Solution()

result = solution_instance.firstPalindrome(input_words)
print(result)