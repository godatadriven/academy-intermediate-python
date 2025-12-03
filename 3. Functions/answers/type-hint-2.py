import pandas as pd

def validate_column_types(df, expected_types):
    """
    Validate that DataFrame columns match expected types.
    
    Args:
        df: pandas DataFrame to validate
        expected_types: dict mapping column names to expected types
                       e.g., {'age': 'int64', 'name': 'object', 'salary': 'float64'}
    
    Returns:
        True if all types match, raises ValueError with details if not
    """
    try:
        # Check if df is actually a DataFrame
        if not isinstance(df, pd.DataFrame):
            raise AttributeError("Input is not a pandas DataFrame")
        
        # Check for missing columns
        missing_cols = set(expected_types.keys()) - set(df.columns)
        if missing_cols:
            raise KeyError(f"Expected columns not found in DataFrame: {missing_cols}")
        
        # Check data types
        type_mismatches = {}
        for col, expected_type in expected_types.items():
            actual_type = str(df[col].dtype)
            if actual_type != expected_type:
                type_mismatches[col] = {
                    'expected': expected_type,
                    'actual': actual_type
                }
        
        if type_mismatches:
            error_msg = "Column type mismatches found:\n"
            for col, types in type_mismatches.items():
                error_msg += f"  - {col}: expected {types['expected']}, got {types['actual']}\n"
            raise ValueError(error_msg)
        
        print("✓ All column types validated successfully!")
        return True
    
    except AttributeError as e:
        print(f"AttributeError: {e}")
        raise
    
    except KeyError as e:
        print(f"KeyError: {e}")
        raise
    
    except ValueError as e:
        print(f"ValidationError: {e}")
        raise
    
    except Exception as e:
        print(f"Unexpected error during validation: {e}")
        raise

# Test cases:
df = pd.DataFrame({
    'age': [25, 30, 35],
    'name': ['Alice', 'Bob', 'Charlie'],
    'salary': [50000.0, 60000.0, 55000.0]
})

# This should pass
expected = {'age': 'int64', 'name': 'object', 'salary': 'float64'}
validate_column_types(df, expected)

# This should raise ValueError
try:
    wrong_types = {'age': 'float64', 'name': 'object'}
    validate_column_types(df, wrong_types)
except ValueError as e:
    print(f"Caught expected error: {e}")

# This should raise KeyError
try:
    missing = {'age': 'int64', 'missing_column': 'object'}
    validate_column_types(df, missing)
except KeyError as e:
    print(f"Caught expected error: {e}")