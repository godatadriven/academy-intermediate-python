ages = [25, 150, 30, -5, 42, 200, 18, 0, 99, -10, 65]

# Solution: List comprehension with if/else for valid age range
cleaned_ages = [age if 0 <= age <= 120 else None for age in ages]

print("Cleaned ages:")
print(cleaned_ages)
# Output: [25, None, 30, None, 42, None, 18, 0, 99, None, 65]

print("\n" + "="*60)

# Bonus: Replace invalid ages with median of valid ages
valid_ages = [age for age in ages if 0 <= age <= 120]
median_age = sorted(valid_ages)[len(valid_ages) // 2]

cleaned_with_median = [age if 0 <= age <= 120 else median_age for age in ages]

print(f"Valid ages: {valid_ages}")
print(f"Median age: {median_age}")
print(f"Cleaned with median: {cleaned_with_median}")