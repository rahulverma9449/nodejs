from collections import Counter
# class Solution:
# 	def find_duplicate(self, arr):
# 		l = []
# 		d = Counter(arr)
# 		for i in d.keys():
# 			if d[i]>1:
# 				l.append(i)
# 		if len(l)==0:
# 			l.append(-1)
# 		l.sort()
# 		return l
# solution = Solution()
# list = [2,3,4,5,6,5,4,3,2]
# result = solution.find_duplicate(list)
# print(result)

###########

class Solution:
	def find_dup(self, arr):
		l = []
		d = Counter(arr)
		for i in d.keys():
			if d[i]> 1:
				l.append(i)
		if len(l)==0:
			l.append(-1)
		l.sort()

		return l

solution = Solution()
list = [2,3,4,5,6,5,4,3,2]
result = solution.find_dup(list)
print(result)