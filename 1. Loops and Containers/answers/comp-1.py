# ex-practical-list.py
"""
Solution for Exercise 1: Extract Numeric Columns
"""

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Carol', 'Dan', 'Eve'],
    'age': [25, 30, 35, 28, 42],
    'email': ['alice@example.com', 'bob@example.com', 'carol@example.com', 'dan@example.com', 'eve@example.com'],
    'salary': [50000.0, 60000.0, 55000.0, 48000.0, 72000.0],
    'is_active': [True, True, False, True, True]
})

print("DataFrame info:")
print(df.dtypes)
print("\n" + "="*60)

# Solution: List comprehension to get numeric columns
numeric_columns = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]

print(f"Numeric columns: {numeric_columns}")
# Output: ['user_id', 'age', 'salary']

print("\n" + "="*60)

# Bonus: Only float columns
float_columns = [col for col in df.columns if df[col].dtype == 'float64']
print(f"Float columns (bonus): {float_columns}")
# Output: ['salary']

# Alternative solution using str() for type checking
numeric_columns_alt = [col for col in df.columns if str(df[col].dtype) in ['int64', 'float64']]
print(f"Numeric columns (alternative): {numeric_columns_alt}")