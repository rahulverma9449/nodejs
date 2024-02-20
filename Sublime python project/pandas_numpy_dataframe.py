import pandas as pd
import numpy as np

# Creating data using Python dictionary
data = {
    'Student Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Student ID': [101, 102, 103, 104, 105],
    'Student Percentage': np.random.uniform(60, 100, 5)  # Generating random percentages between 60 and 100
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
