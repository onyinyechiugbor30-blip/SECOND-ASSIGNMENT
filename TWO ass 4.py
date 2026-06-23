'''QUESTION 4 — Robust Password & Username Validator
Topics: Functions · Strings · Loops · Conditions

Write a function `validate_credentials(username, password)` that returns a dictionary with validation results.  
Checks must include:
Username: 6+ characters, no spaces, starts with letter.
Password: 8+ chars, has uppercase, lowercase, digit, special char.
Use nested ifs and loops to count character types.
Return specific error messages for each failed rule.
Create a generate_suggestions(password) function that gives improvement tips.

Test with 6 different combinations (some valid, many invalid).'''

# Function to check if a username and password are valid
def validate_credentials(username, password):
    # we'll use a dictionary to store all validation results
    results = {}
    # USERNAME VALIDATION
    # Check if username has at least 6 characters
    if len(username) >= 6:
        # Check if username contains spaces
        if " " not in username:
            # Check if first character is a letter
            if username[0].isalpha():
                results["Username"] = "Valid"
                #if username does not start with letter, let the result be 
            else:
                results["Username"] = "Username must start with a letter."
                #if username contains spaces, let the result be
        else:
            results["Username"] = "Username must not contain spaces."
            #if username is not up to six characters, the result should be,
    else:
        results["Username"] = "Username must be at least 6 characters long."

    # PASSWORD VALIDATION
    # Counting for different character types
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0
    # Special characters allowed
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    # Go through each character in the password
    for character in password:
        # Count uppercase letters
        if character.isupper():
            uppercase_count += 1
        # Count lowercase letters
        elif character.islower():
            lowercase_count += 1
        # Count digits
        elif character.isdigit():
            digit_count += 1
        # Count special characters
        elif character in special_characters:
            special_count += 1
    # create empty List to store password errors
    password_errors = []
    # Check password length(len is used to check length)
    #append is used to add
    if len(password) < 8:
        password_errors.append("Password must be at least 8 characters long.")
    # Check for uppercase letter
    if uppercase_count == 0:
        password_errors.append("Password needs at least one uppercase letter.")
    # Check for lowercase letter
    if lowercase_count == 0:
        password_errors.append("Password needs at least one lowercase letter.")
    # Check for digit
    if digit_count == 0:
        password_errors.append("Password needs at least one number.")
    # Check for special character
    if special_count == 0:
        password_errors.append("Password needs at least one special character.")
    # If there are no password errors
    if len(password_errors) == 0:
        results["Password"] = "Valid"
    # Otherwise store all errors
    else:
        results["Password"] = password_errors
    # Return the completed dictionary
    return results
# Function to suggest improvements for a password
def generate_suggestions(password):
    print("Suggestions:")
    # Check password length
    if len(password) < 8:
        print("- Make the password at least 8 characters long.")
    # Check for uppercase letter
    has_uppercase = False
    for character in password:
        if character.isupper():
            has_uppercase = True
    if not has_uppercase:
        print("- Add at least one uppercase letter.")
    # Check for lowercase letter
    has_lowercase = False
    for character in password:
        if character.islower():
            has_lowercase = True
    if not has_lowercase:
        print("- Add at least one lowercase letter.")
    # Check for digit
    has_digit = False
    for character in password:
        if character.isdigit():
            has_digit = True
    if not has_digit:
        print("- Add at least one number.")
    # Check for special character
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    has_special = False
    for character in password:
        if character in special_characters:
            has_special = True
    if not has_special:
        print("- Add at least one special character.")

    print()

# TEST CASES

test_data = [
     # Valid because username starts with letter, is up least six characters, and does not contain empty space
     #also valid because password is up to 8 characters, contains digit, uppercase, lowercase and special character
    ("Onyinyechi", "StrongP@ass3"), 
    #many errors because it does not meet the requirements for valid password and username
    ("John", "abc"),  
    # Username contains space
    ("De borah", "Pasho6rd!"),  
    # Username starts with number
    ("123User", "Pass3w#ord"),  
    # No uppercase in password
    ("Austin22", "jass3$wogd!"),  
    # No lowercase in password
    ("Wisdom55", "TH3DGT>")  
]
# Test all username and password combinations
for username, password in test_data:
    print("\nUsername:", username)
    print("Password:", password)
    result = validate_credentials(username, password)
    print("Validation Result:")
    print(result)
    # If password is not valid, show suggestions
    if result["Password"] != "Valid":
        generate_suggestions(password)