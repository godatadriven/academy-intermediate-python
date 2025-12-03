# ex-practical-dict.py
"""
Solution for Exercise 2: Column Data Type Mapping
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

# Solution: Dictionary comprehension mapping columns to types
column_types = {col: str(dtype) for col, dtype in df.dtypes.items()}

print("Column types:")
for col, dtype in column_types.items():
    print(f"  {col}: {dtype}")

# Expected output:
# Column types:
#   user_id: int64
#   name: object
#   age: int64
#   email: object
#   salary: float64
#   is_active: bool

print("\n" + "="*60)

# Bonus 1: Only numeric columns
numeric_column_types = {col: str(dtype) for col, dtype in df.dtypes.items() 
                        if str(dtype) in ['int64', 'float64']}

print("\nBonus 1 - Numeric columns only:")
for col, dtype in numeric_column_types.items():
    print(f"  {col}: {dtype}")
# Output:
#   user_id: int64
#   age: int64
#   salary: float64

print("\n" + "="*60)

# Bonus 2: Group columns by data type
# Method 1: Using a loop to build the dictionary
type_to_columns = {}
for col, dtype in df.dtypes.items():
    dtype_str = str(dtype)
    if dtype_str not in type_to_columns:
        type_to_columns[dtype_str] = []
    type_to_columns[dtype_str].append(col)

print("\nBonus 2 - Columns grouped by type (Method 1):")
for dtype, cols in type_to_columns.items():
    print(f"  {dtype}: {cols}")

# Method 2: Using setdefault (more Pythonic)
type_to_columns_v2 = {}
for col, dtype in df.dtypes.items():
    type_to_columns_v2.setdefault(str(dtype), []).append(col)

print("\nBonus 2 - Columns grouped by type (Method 2 - setdefault):")
for dtype, cols in type_to_columns_v2.items():
    print(f"  {dtype}: {cols}")

# Method 3: Using defaultdict (most elegant)
from collections import defaultdict

type_to_columns_v3 = defaultdict(list)
for col, dtype in df.dtypes.items():
    type_to_columns_v3[str(dtype)].append(col)

print("\nBonus 2 - Columns grouped by type (Method 3 - defaultdict):")
for dtype, cols in type_to_columns_v3.items():
    print(f"  {dtype}: {cols}")

# Expected output for all Bonus 2 methods:
#   int64: ['user_id', 'age']
#   object: ['name', 'email']
#   float64: ['salary']
#   bool: ['is_active']