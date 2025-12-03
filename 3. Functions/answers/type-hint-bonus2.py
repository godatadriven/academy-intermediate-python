## BONUS: Advanced version with verbose parameter and error tracking

def load_csv_with_types_advanced(filepath, column_types, required_columns=None, 
                                 fillna_strategy=None, verbose=True):
    """
    Load a CSV file with robust error handling and automatic type casting.
    Returns both the dataframe and a list of any issues encountered.
    
    Args:
        filepath: Path to the CSV file
        column_types: dict mapping column names to desired types
        required_columns: list of columns that must exist (optional)
        fillna_strategy: dict mapping column names to fill values (optional)
        verbose: Whether to print status messages (default: True)
    
    Returns:
        tuple: (DataFrame or None, list of error/warning messages)
    """
    errors = []
    
    def log(message, is_error=False):
        """Helper to log messages and track errors"""
        if verbose:
            print(message)
        if is_error:
            errors.append(message)
    
    try:
        log(f"Loading CSV from: {filepath}")
        df = pd.read_csv(filepath)
        log(f"✓ Loaded {len(df)} rows, {len(df.columns)} columns")
        
        if required_columns:
            missing = set(required_columns) - set(df.columns)
            if missing:
                raise ValueError(f"Missing required columns: {missing}")
            log(f"✓ All {len(required_columns)} required columns present")
        
        if fillna_strategy:
            for col, fill_value in fillna_strategy.items():
                if col in df.columns:
                    na_count = df[col].isna().sum()
                    df[col].fillna(fill_value, inplace=True)
                    log(f"✓ Filled {na_count} NaN values in '{col}' with {fill_value}")
        
        for col, dtype in column_types.items():
            if col not in df.columns:
                msg = f"Column '{col}' not found, skipping type cast"
                log(f"⚠ Warning: {msg}", is_error=True)
                continue
            
            try:
                df[col] = df[col].astype(dtype)
                log(f"✓ Cast '{col}' to {dtype.__name__}")
            except (ValueError, TypeError) as e:
                msg = f"Could not cast '{col}' to {dtype.__name__}: {str(e)[:50]}"
                log(f"⚠ Warning: {msg}", is_error=True)
        
        log(f"\n✓ Load completed with {len(errors)} warning(s)")
        return df, errors
    
    except FileNotFoundError:
        msg = f"File not found: {filepath}"
        log(f"✗ {msg}", is_error=True)
        return None, errors
    
    except pd.errors.EmptyDataError:
        msg = f"CSV file is empty: {filepath}"
        log(f"✗ {msg}", is_error=True)
        return None, errors
    
    except ValueError as e:
        msg = f"Validation error: {e}"
        log(f"✗ {msg}", is_error=True)
        errors.append(msg)
        raise
    
    except Exception as e:
        msg = f"Unexpected error: {e}"
        log(f"✗ {msg}", is_error=True)
        errors.append(msg)
        raise

# Test the advanced version:
df, errors = load_csv_with_types_advanced(
    'data/pokemon.csv',
    column_types={'hp': int, 'name': str, 'attack': int},
    required_columns=['name', 'hp'],
    fillna_strategy={'hp': 0},
    verbose=True
)

print(f"\nEncountered {len(errors)} issues during loading")
if errors:
    print("Issues:")
    for err in errors:
        print(f"  - {err}")