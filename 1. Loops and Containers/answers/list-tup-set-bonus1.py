# exercise1_deduplicate_customers_bonus.py
"""
Bonus solution for Exercise 1: Deduplicating Customer Records
Handles None/empty emails, configurable keep strategy, and returns duplicate count
"""

def deduplicate_customers_bonus(customer_list, keep='last'):
    """
    Remove duplicate customers based on email, keeping first or last record.
    
    Args:
        customer_list: List of dictionaries containing customer data
        keep: Either 'first' or 'last' to control which duplicate to keep
    
    Returns:
        tuple: (list of unique customers, number of duplicates found)
    """
    email_to_customer = {}
    duplicate_count = 0
    
    for customer in customer_list:
        email = customer.get('email')
        
        # Handle None or empty emails - keep all of them
        if not email or email == '':
            # Generate a unique key for customers without emails
            # Using id() ensures each one is treated as unique
            unique_key = f"__no_email_{id(customer)}__"
            email_to_customer[unique_key] = customer
            continue
        
        # If email not seen before, add it
        if email not in email_to_customer:
            email_to_customer[email] = customer
        else:
            duplicate_count += 1
            
            if keep == 'last':
                # Compare dates and keep the more recent one
                existing_date = email_to_customer[email]['signup_date']
                current_date = customer['signup_date']
                
                if current_date > existing_date:
                    email_to_customer[email] = customer
            elif keep == 'first':
                # Keep the existing one (do nothing)
                pass
            else:
                raise ValueError(f"keep must be 'first' or 'last', got '{keep}'")
    
    return list(email_to_customer.values()), duplicate_count


# Test data
customers = [
    {'name': 'Alice Johnson', 'email': 'alice@email.com', 'signup_date': '2024-01-15', 'plan': 'basic'},
    {'name': 'Bob Smith', 'email': 'bob@email.com', 'signup_date': '2024-02-20', 'plan': 'premium'},
    {'name': 'Alice J.', 'email': 'alice@email.com', 'signup_date': '2024-03-10', 'plan': 'premium'},
    {'name': 'Carol White', 'email': 'carol@email.com', 'signup_date': '2024-01-05', 'plan': 'basic'},
    {'name': 'Bob Smith', 'email': 'bob@email.com', 'signup_date': '2024-03-15', 'plan': 'enterprise'},
    {'name': 'Dan Unknown', 'email': None, 'signup_date': '2024-01-01', 'plan': 'basic'},
    {'name': 'Eve Mystery', 'email': '', 'signup_date': '2024-01-02', 'plan': 'basic'},
]

print("Testing with keep='last':")
unique_customers, dup_count = deduplicate_customers_bonus(customers, keep='last')
print(f"Original: {len(customers)} customers")
print(f"After deduplication: {len(unique_customers)} customers")
print(f"Duplicates found: {dup_count}")
print("\nUnique customers:")
for customer in unique_customers:
    print(f"  {customer['name']} ({customer.get('email', 'NO EMAIL')}) - {customer['plan']} - {customer['signup_date']}")

print("\n" + "="*60)
print("Testing with keep='first':")
unique_customers, dup_count = deduplicate_customers_bonus(customers, keep='first')
print(f"After deduplication: {len(unique_customers)} customers")
print(f"Duplicates found: {dup_count}")
print("\nUnique customers:")
for customer in unique_customers:
    print(f"  {customer['name']} ({customer.get('email', 'NO EMAIL')}) - {customer['plan']} - {customer['signup_date']}")