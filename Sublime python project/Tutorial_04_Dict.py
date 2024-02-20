# Example of a dictionary
student = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A',
    'courses': ['Math', 'Physics', 'Computer Science']
}

# Accessing values using keys
print("Student Name:", student['name'])  # Output: Student Name: Alice
print("Age:", student['age'])  # Output: Age: 20

# Modifying values
student['grade'] = 'B'
print("Updated Grade:", student['grade'])  # Output: Updated Grade: B

# Adding a new key-value pair
student['city'] = 'New York'
print("City:", student['city'])  # Output: City: New York

# Iterating through keys and values
for key, value in student.items():
    print(key, ":", value)