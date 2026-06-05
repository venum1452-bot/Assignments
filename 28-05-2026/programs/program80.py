import re

def is_valid_password(password):
    # Check length
    if not (6 <= len(password) <= 12):
        return False
    
    # Check all required conditions
    if not re.search("[a-z]", password):   # at least one lowercase
        return False
    if not re.search("[A-Z]", password):   # at least one uppercase
        return False
    if not re.search("[0-9]", password):   # at least one digit
        return False
    if not re.search("[$#@]", password):   # at least one special char
        return False
    
    return True

# Input passwords
passwords = input("Enter passwords separated by commas: ").split(',')

# Collect valid ones
valid_passwords = [psw for psw in passwords if is_valid_password(psw)]

# Output
print(",".join(valid_passwords))
