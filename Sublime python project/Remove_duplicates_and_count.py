def remove_duplicates_and_count(string):
    char = {}
    unique_str = ""
    for i in string:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
            unique_str += i
     
    return unique_str,char
  
input_str = "programming"
output_unique_str, output_char_count = remove_duplicates_and_count(input_str)

print(f"Input String: {input_str}")
print(f"String without duplicates:{output_unique_str}")

print(f"character Counts: ")

for i, count in output_char_count.items():
    print(f"{i}: {count}")
 
 ####################   
    
def remove_duplicates(input_list):
    unique_set = set()
    result_list = []

    for item in input_list:
        if item not in unique_set:
            result_list.append(item)
            unique_set.add(item)

    return result_list

# Example usage:
input_strings = ["apple", "banana", "orange", "apple", "grape", "banana"]
unique_strings = remove_duplicates(input_strings)

print("Original List:", input_strings)
print("List with Duplicates Removed:", unique_strings)
