# # Approch_1

# def reverse_number(num):
# 	reverse_num = int(str(num)[::-1])
# 	return reverse_num
#
# input =  123456
# result = reverse_number(input)
# print(result)

# ## Approch_02


# def reverse(num):
# 	reversed = 0

# 	while num > 0:
# 		reminder = num % 10
# 		reversed = (reversed * 10) + reminder

# 		num  = num // 10

# 	return reversed


## Approch_03

# def reverse_data(num):
# 	if num < 10:
# 		return num
# 	else:
# 		return int(str(num % 10) + str(reverse_data(num // 10)))
#
intput =  1234
# # result = reverse_number(intput)
# # result1 = reverse(intput)
# result3 = reverse_data(intput)
#
# # print(result1)
# # print(f"The reverse of {intput} is : {result}")
# print(result3)