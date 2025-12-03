import pandas as pd

def load_csv_with_types(filepath, column_types, required_columns=None, fillna_strategy=None):
    """
    Load a CSV file with robust error handling and automatic type casting.
    
    Args:
        filepath: Path to the CSV file
        column_types: dict mapping column names to desired types
                     e.g., {'age': int, 'name': str, 'score': float}
        required_columns: list of columns that must exist (optional)
        fillna_strategy: dict mapping column names to fill values (optional)
                        e.g., {'age': 0, 'score': -1}
    
    Returns:
        DataFrame with properly typed columns, or None if loading fails
    """
    try:
        # Step 1: Load the CSV
        print(f"Loading CSV from: {filepath}")
        df = pd.read_csv(filepath)
        print(f"✓ Loaded {len(df)} rows")
        
        # Step 2: Validate required columns
        if required_columns:
            missing = set(required_columns) - set(df.columns)
            if missing:
                raise ValueError(f"Missing required columns: {missing}")
            print(f"✓ All required columns present")
        
        # Step 3: Fill NA values if strategy provided
        if fillna_strategy:
            for col, fill_value in fillna_strategy.items():
                if col in df.columns:
                    df[col].fillna(fill_value, inplace=True)
                    print(f"✓ Filled NaN values in '{col}' with {fill_value}")
        
        # Step 4: Cast column types
        casting_errors = []
        for col, dtype in column_types.items():
            if col not in df.columns:
                print(f"⚠ Warning: Column '{col}' not found in data, skipping type cast")
                continue
            
            try:
                df[col] = df[col].astype(dtype)
                print(f"✓ Cast '{col}' to {dtype.__name__}")
            except (ValueError, TypeError) as e:
                warning = f"Could not cast '{col}' to {dtype.__name__}: {e}"
                print(f"⚠ Warning: {warning}")
                casting_errors.append(warning)
                # Keep original type instead of failing
        
        if casting_errors:
            print(f"\n⚠ Completed with {len(casting_errors)} casting warning(s)")
        else:
            print("\n✓ All type casting successful!")
        
        return df
    
    except FileNotFoundError as e:
        print(f"✗ File not found: {filepath}")
        return None
    
    except pd.errors.EmptyDataError as e:
        print(f"✗ CSV file is empty: {filepath}")
        return None
    
    except ValueError as e:
        print(f"✗ Validation error: {e}")
        raise  # Re-raise because missing required columns is serious
    
    except Exception as e:
        print(f"✗ Unexpected error loading data: {e}")
        raise  # Re-raise unexpected errors for debugging

# Test it with Pokemon data:
df = load_csv_with_types(
    'data/pokemon.csv',
    column_types={'hp': int, 'name': str, 'attack': int},
    required_columns=['name', 'hp'],
    fillna_strategy={'hp': 0}
)

if df is not None:
    print("\n" + "="*50)
    print("Final DataFrame Info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())