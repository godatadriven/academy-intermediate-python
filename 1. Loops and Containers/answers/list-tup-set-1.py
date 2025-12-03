# exercise1_deduplicate_customers.py
"""
Model solution for Exercise 1: Deduplicating Customer Records
"""

def deduplicate_customers(customer_list):
    """
    Remove duplicate customers based on email, keeping the most recent record.
    
    Args:
        customer_list: List of dictionaries containing customer data
    
    Returns:
        List of deduplicated customer dictionaries
    """
    # Dictionary to track the most recent customer by email
    email_to_customer = {}
    
    for customer in customer_list:
        email = customer['email']
        
        # If email not seen before, add it
        if email not in email_to_customer:
            email_to_customer[email] = customer
        else:
            # Compare dates and keep the more recent one
            existing_date = email_to_customer[email]['signup_date']
            current_date = customer['signup_date']
            
            if current_date > existing_date:
                email_to_customer[email] = customer
    
    # Return list of unique customers
    return list(email_to_customer.values())


# Test data
customers = [
    {'name': 'Alice Johnson', 'email': 'alice@email.com', 'signup_date': '2024-01-15', 'plan': 'basic'},
    {'name': 'Bob Smith', 'email': 'bob@email.com', 'signup_date': '2024-02-20', 'plan': 'premium'},
    {'name': 'Alice J.', 'email': 'alice@email.com', 'signup_date': '2024-03-10', 'plan': 'premium'},
    {'name': 'Carol White', 'email': 'carol@email.com', 'signup_date': '2024-01-05', 'plan': 'basic'},
    {'name': 'Bob Smith', 'email': 'bob@email.com', 'signup_date': '2024-03-15', 'plan': 'enterprise'},
]

# Test the function
unique_customers = deduplicate_customers(customers)
print(f"Original: {len(customers)} customers")
print(f"After deduplication: {len(unique_customers)} customers")
print("\nUnique customers:")
for customer in unique_customers:
    print(f"  {customer['name']} ({customer['email']}) - {customer['plan']}")