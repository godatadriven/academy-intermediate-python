def safe_divide(numerator, dividend, default=None):
    """
    Safely divide two numbers with proper error handling.
    
    Args:
        numerator: The number to divide
        dividend: The number to divide by
        default: Value to return if division fails (default: None)
    
    Returns:
        Result of division, or default value if it fails
    """
    try:
        # Try to convert inputs to float and perform division
        result = float(numerator) / float(dividend)
        return result
    
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero: {e}")
        return default
    
    except (TypeError, ValueError) as e:
        print(f"Invalid input types - cannot convert to numbers: {e}")
        return default
    
    except Exception as e:
        print(f"Unexpected error during division: {e}")
        raise  # Re-raise unexpected errors for debugging

# Test cases:
print(safe_divide(10, 2))           # 5.0
print(safe_divide(10, 0))           # Cannot divide by zero, returns None
print(safe_divide("10", "2"))       # 5.0 (converts strings)
print(safe_divide("ten", 2))        # Invalid input, returns None
print(safe_divide([1,2], 3))        # Invalid input, returns None
print(safe_divide(10, 0, default=0))  # Returns 0 as default