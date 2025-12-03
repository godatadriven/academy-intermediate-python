# exercise2_pipeline_validation.py
"""
Model solution for Exercise 2: Data Pipeline Validation
"""

def validate_pipeline_columns(previous_columns, current_columns, stage_name, 
                              allow_additions=False, allow_removals=False):
    """
    Validate that column changes between pipeline stages are intentional.
    
    Args:
        previous_columns: List/set of column names from previous stage
        current_columns: List/set of column names from current stage
        stage_name: Name of current stage (for error messages)
        allow_additions: Whether new columns are allowed (default: False)
        allow_removals: Whether removing columns is allowed (default: False)
    
    Returns:
        tuple: (is_valid: bool, report: dict with 'added', 'removed', 'message' keys)
    """
    # Convert to sets for efficient set operations
    prev_set = set(previous_columns)
    curr_set = set(current_columns)
    
    # Find what changed
    added = curr_set - prev_set
    removed = prev_set - curr_set
    
    # Check if changes are valid
    is_valid = True
    messages = []
    
    if added and not allow_additions:
        is_valid = False
        messages.append(f"X Unexpected columns added: {sorted(added)}")
    elif added:
        messages.append(f"✓ Columns added (allowed): {sorted(added)}")
    
    if removed and not allow_removals:
        is_valid = False
        messages.append(f"X Unexpected columns removed: {sorted(removed)}")
    elif removed:
        messages.append(f"✓ Columns removed (allowed): {sorted(removed)}")
    
    if not added and not removed:
        messages.append(f"✓ No column changes in {stage_name}")
    
    # Build report
    report = {
        'added': sorted(added),
        'removed': sorted(removed),
        'message': ' | '.join(messages) if messages else f"No changes in {stage_name}"
    }
    
    return is_valid, report


# Test data
stage_1_columns = ['user_id', 'name', 'email', 'signup_date', 'country']
stage_2_columns = ['user_id', 'name', 'email', 'signup_date', 'country', 'age']
stage_3_columns = ['user_id', 'email', 'signup_date', 'country', 'age']
stage_4_columns = ['user_id', 'email', 'country', 'age']

print("Stage 1 → Stage 2 (additions allowed):")
is_valid, report = validate_pipeline_columns(stage_1_columns, stage_2_columns, 
                                             "Stage 2", allow_additions=True)
print(f"Valid: {is_valid}")
print(f"Report: {report}")

print("\n" + "="*60)
print("Stage 2 → Stage 3 (no changes allowed):")
is_valid, report = validate_pipeline_columns(stage_2_columns, stage_3_columns, 
                                             "Stage 3")
print(f"Valid: {is_valid}")
print(f"Report: {report}")

print("\n" + "="*60)
print("Stage 3 → Stage 4 (removals allowed):")
is_valid, report = validate_pipeline_columns(stage_3_columns, stage_4_columns, 
                                             "Stage 4", allow_removals=True)
print(f"Valid: {is_valid}")
print(f"Report: {report}")