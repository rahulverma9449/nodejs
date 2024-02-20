txt = "apple##$orarrrrrnge$"
first_hash = txt.find("#")
second_hash = txt.find("#")
third_dollar = txt.find("$")

print("position of 1st hash:", first_hash )
print("position of 2nd hash:", second_hash + 1)
print("position of 3rd dollar:", third_dollar )
print(third_dollar + 1)