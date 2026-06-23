'''Question 1
Create a function encrypt_name(full_name, key) that shifts each letter by the key value (key = length of your first name).  
Add these features:
 Handle both uppercase and lowercase.
 Preserve spaces and punctuation.
 If the key is even, also reverse the entire string after shifting.
 Write a `decrypt_name(encrypted_text, key)` function that reverses the process.
 In the main program, test both functions and show the full cycle (original → encrypted → decrypted).'''

#Write Function to encrypt name
def encrypt_name(full_name, key):
    # Store all lowercase letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # create an empty string to store encrypted text
    encrypted_text = ""
    # Go through each character one by one
    for character in full_name:
        # Check if the character is a lowercase letter
        if character.islower():
            # Find the position of the letter
            position = alphabet.index(character)
            # Move forward by the length of the key
            new_position = (position + key) % 26
            # Add the new letter to the encrypted text
            encrypted_text += alphabet[new_position]
        # Check if the character is an uppercase letter
        elif character.isupper():
            # Convert to lowercase so we can find it
            lower_letter = character.lower()
            # Find its position
            position = alphabet.index(lower_letter)
            # Move forward by the key value
            new_position = (position + key) % 26
            # Convert back to uppercase
            encrypted_text += alphabet[new_position].upper()
        # If it is not a letter (space, comma, full stop, etc.)
        else:
            # Keep it exactly the same
            encrypted_text += character
    # If the key is an even number
    if key % 2 == 0:
        # Reverse the whole encrypted text
        encrypted_text = encrypted_text[::-1]
        print("after reversing:", encrypted_text)
    # Send the encrypted text back
    return encrypted_text

# write Function to decrypt  name
def decrypt_name(encrypted_text, key):
    # Store all lowercase letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # If the key is even
    if key % 2 == 0:
        # Undo the reversal first. ::-1 helps to undo reversal
        encrypted_text = encrypted_text[::-1]
        
    # create empty string to store decrypted text
    decrypted_text = ""
    # Go through every character
    for character in encrypted_text:
        # Check for lowercase letters
        if character.islower():
            # Find the letter position
            position = alphabet.index(character)
            # Move backward by the key value
            new_position = (position - key) % 26
            # Add the original letter
            decrypted_text += alphabet[new_position]
        # Check for uppercase letters
        elif character.isupper():
            # Convert to lowercase first
            lower_letter = character.lower()
            # Find the position
            position = alphabet.index(lower_letter)
            # Move backward by the key value
            new_position = (position - key) % 26
            # Convert back to uppercase
            decrypted_text += alphabet[new_position].upper()
        # If any of the character is not a letter
        else:
            # Keep it unchanged
            decrypted_text += character
    # Send back the original text
    return decrypted_text
# Store the first name
first_name = "Onyinyechi"
# Store the last name
last_name = "Ugbor"
# Join them together to create the full name
full_name = first_name + " " + last_name
# Key is the length of the first name
key = len(first_name)
# Encrypt the full name
encrypted_name = encrypt_name(full_name, key)
# Decrypt the encrypted name
decrypted_name = decrypt_name(encrypted_name, key)
# Show all the results
print("Original Name is :", full_name)
print("Key Used is      :", key)
print("Encrypted Name is:", encrypted_name)
print("Decrypted Name is:", decrypted_name)