# ==================================================
# ==================================================
#               String functions
# ==================================================
# ==================================================






# Create a string variable with whitespaces in it
# Remove whitespaces from left side
# Remove whitespaces from right side
# Remove whitespaces from both sides
# Capitalize first letter of the string
# Convert whole string to uppercase
# Convert whole string to lowercase
# Convert a list of words to string seperated by spaces
# Convert a string into a list
# Count word occurence in a string
# Retrieve index of matching word in a string
# Replace words inside of string


# Create a string with whitespaces
str = "    this is a string with whtiespaces       "

# Remove whitespace from left side
print("String without left whitespace:", str.lstrip())

# Remove whitespace from right side
print("String without right whitespace:", str.rstrip())

# Remove whitespace from both sides
print("String without whitespace:", str.strip())

# For further action removing whitespace from string
str = str.strip()

# Capitalize first letter of string
print("Capitalized string:", str.capitalize())

# Convert whole string to lowercase
print("Uppercase string:", str.upper())

# Convert whole string to uppercase
print("lowercase string:", str.lower())

# convert a list of words to string
listOfWords = ['Jayant', 'Malik', 'is', 'a', 'programmer']
result = " ".join(listOfWords)

# Print result
print("list converted to string:", result)

# Convert a string into a list of words
listOfWords = []
listOfWords = str.split()

# Printing list of words
print("string to list of words:", listOfWords)

# Count a word occurence in a string
print("no. of words in a string:", str.count("is"))

# Retrieve index of matching word in a string
print("is is at index:", str.find("is"))

# Replace words inside of string
print("is replaced with:", str.replace("is", "with"))


# ============================================
# Create an acronym generator:
# The words in resultant acronym must be uppercase

# Sample output:
# Enter a bunch of words to calculate acronymm: Random Access Memory
# Acronymm: RAM


# Ask the user for complete string to generate acronym
userWords = input("Enter a bunch of words to generate acronymm: ")

# Convert the user entered words in a list
list = []

# Add string into the list
list = userWords.split()

# Create a variable to hold acronym
acronym = ""
# Navigate through the list and get first letter of the each item
for item in list:
    acronym += item[0].upper()

print("Acronym:", acronym)


# ===================================================
# Check if a string is alphabet
# Check if a string is alphabetic or numeric (alphanumeric)
# Check if a string is a space
# Check if a string is a numeric
# Check if a string is a decimal
# Check if a string is a digit
# Check if a string is an identifier
# Check if a character is printable
# Check string case: title, upper, lower


# Check if a string is character
print("is 'ABC' alphabet:", "ABC".isalpha())

# Check if a string is alphanumeric
print("is 'ABC5' alphanumeric:", "ABC4".isalnum())

# Check if a string is a space
print("is ' ' a space:", " ".isspace())

# Check if a string is a numeric
print("is '423' is number:", "423".isnumeric())

# Check if a string is a decimal
print("is '34.32' a decimal:", "34.32".isdecimal())

# Check if a string is a digit
print("is '25' a digit:", "25".isdigit())

# Check if a string is an identifier
print("is '-' an identifier:", "-".isidentifier())

# Check if a character is printable
print("is '\\0' printable:", "\0".isprintable())

# Check string case: title, upper, lower
print("is 'Word' title case:", "Word".istitle())
print("is 'WORD' upper case:", "WORD".isupper())
print("is 'data' lower case:", "data".islower())


# ===================================================
# Create a function to check if a number if float
# Use exception handling in the function

def isfloat(str):
    try:
        float(str)
        return True
    except:
        return False

print("is 3.14 a float:", isfloat(3.14))


# ======================================================
# Create a Caesar cipher. Encryption program

# Rules:
# Do not change any character if it is not a letter. Keep it as it is.
# Ask the user for no of characters to shift.

# Algorithm:
# Any letter that is entered shifts n position as entered by the user.
# if user enters 3 then
# A becomes D, B becomes E

# Unicodes for character:
# A - Z : 65 - 90
# a - z : 97 - 122


# Ask the user for message and no of characters to shift
message = input("Enter message: ")
key = int(input("Enter no of position to shift: "))

# Prepare the secret_message
secretMessage = ""

# Cycle through each character in message
for character in message:

# If character is a letter:
    if character.isalpha():

        # If character is upper case
        if character.isupper():
        # Check if the character is larger then Z:
            if ord(character) >= 90:

            # Subtract 26 from the letter
                newCharacterCode = ord(character) - 26 + key
                secretMessage += chr(newCharacterCode)

        # Else if the character is smaller then A:
            elif ord(character) < 65:

            # Add 26 to the letter
                newCharacterCode = ord(character) + 26 + key
                secretMessage += chr(newCharacterCode)

        # Else encode the character
            else:
                newCharacterCode = ord(character) + key
                secretMessage += chr(newCharacterCode)

        # If character is lower case
        elif character.islower():

            # If character is smaller then a then add 26 to it
            if ord(character) < 97:

                newCharacterCode = ord(character) + 26 + key
                secretMessage += chr(newCharacterCode)

            # Else if character is larger then z then subtract 26 from it.
            elif ord(character) >= 122:

                newCharacterCode = ord(character) - 26 + key
                secretMessage += chr(newCharacterCode)

            # Else encode the character
            else:

                newCharacterCode = ord(character) + key
                secretMessage += chr(newCharacterCode)


# If the character is not a letter
    else:

    # then keep it as it is
        secretMessage += character


# Create an decrypted variable to hold original message
decrypted = ""

# Convert Secret message back to original message
for character in secretMessage:

# If character is a letter:
    if character.isalpha():

        # If character is upper case
        if character.isupper():
        # Check if the character is larger then Z:
            if ord(character) >= 90:

            # Subtract 26 from the letter
                newCharacterCode = ord(character) - 26 - key
                decrypted += chr(newCharacterCode)

        # Else if the character is smaller then A:
            elif ord(character) < 65:

            # Add 26 to the letter
                newCharacterCode = ord(character) + 26 - key
                decrypted += chr(newCharacterCode)

        # Else encode the character
            else:
                newCharacterCode = ord(character) - key
                decrypted += chr(newCharacterCode)

        # If character is lower case
        elif character.islower():

            # If character is smaller then a then add 26 to it
            if ord(character) < 97:

                newCharacterCode = ord(character) + 26 - key
                decrypted += chr(newCharacterCode)

            # Else if character is larger then z then subtract 26 from it.
            elif ord(character) >= 122:

                newCharacterCode = ord(character) - 26 - key
                decrypted += chr(newCharacterCode)

            # Else encode the character
            else:

                newCharacterCode = ord(character) - key
                decrypted += chr(newCharacterCode)


# If the character is not a letter
    else:

    # then keep it as it is
        decrypted += character



# print encrypted and decrypted on screen
print("Encrypted:", secretMessage)
print("Decrypted:", decrypted)


# ======================================================
# print some blank lines
print("\n\n\n\n\n\n\n\n")


# =========================================================
# Create a Caesar cipher. Encryption program by seperating code in functions

def encrypt_message(message, key):
    # Do the encryption
    secretMessage = ""

    # Cycle through each character in message
    for character in message:

        # If character is a letter:
        if character.isalpha():

            # If character is upper case
            if character.isupper():
                # Check if the character is larger then Z:
                if ord(character) >= 90:

                    # Subtract 26 from the letter
                    newCharacterCode = ord(character) - 26 + key
                    secretMessage += chr(newCharacterCode)

                # Else if the character is smaller then A:
                elif ord(character) < 65:

                    # Add 26 to the letter
                    newCharacterCode = ord(character) + 26 + key
                    secretMessage += chr(newCharacterCode)

                # Else encode the character
                else:
                    newCharacterCode = ord(character) + key
                    secretMessage += chr(newCharacterCode)

            # If character is lower case
            elif character.islower():

                # If character is smaller then a then add 26 to it
                if ord(character) < 97:

                    newCharacterCode = ord(character) + 26 + key
                    secretMessage += chr(newCharacterCode)

                # Else if character is larger then z then subtract 26 from it.
                elif ord(character) >= 122:

                    newCharacterCode = ord(character) - 26 + key
                    secretMessage += chr(newCharacterCode)

                # Else encode the character
                else:

                    newCharacterCode = ord(character) + key
                    secretMessage += chr(newCharacterCode)


        # If the character is not a letter
        else:

            # then keep it as it is
            secretMessage += character

    # Return encrypted
    return secretMessage



def decrypt_message(message, key):
    # Do the decryption
    decrypted = ""

    # Convert Secret message back to original message
    for character in message:

        # If character is a letter:
        if character.isalpha():

            # If character is upper case
            if character.isupper():
                # Check if the character is larger then Z:
                if ord(character) >= 90:

                    # Subtract 26 from the letter
                    newCharacterCode = ord(character) - 26 - key
                    decrypted += chr(newCharacterCode)

                # Else if the character is smaller then A:
                elif ord(character) < 65:

                    # Add 26 to the letter
                    newCharacterCode = ord(character) + 26 - key
                    decrypted += chr(newCharacterCode)

                # Else encode the character
                else:
                    newCharacterCode = ord(character) - key
                    decrypted += chr(newCharacterCode)

            # If character is lower case
            elif character.islower():

                # If character is smaller then a then add 26 to it
                if ord(character) < 97:

                    newCharacterCode = ord(character) + 26 - key
                    decrypted += chr(newCharacterCode)

                # Else if character is larger then z then subtract 26 from it.
                elif ord(character) >= 122:

                    newCharacterCode = ord(character) - 26 - key
                    decrypted += chr(newCharacterCode)

                # Else encode the character
                else:

                    newCharacterCode = ord(character) - key
                    decrypted += chr(newCharacterCode)


        # If the character is not a letter
        else:

            # then keep it as it is
            decrypted += character

    # Return the decrypted back
    return decrypted



# Ask user for input
message = input("Enter message to encrypt: ")
key = int(input("Enter no of positions to shift: "))

# Call encrypt and decrypt message to store the results
encrypted = encrypt_message(message, key)
decrypted = decrypt_message(encrypted, key)

# Print the result
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
