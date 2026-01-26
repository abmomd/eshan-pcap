from my_math import add
# A good way to import


import my_math
print(add(1,2))
print(my_math.add(1, 2))
def add(a,b):

    return a + b + 50


# Lists is a collection int, float, string,
# Strings is a collection characters.

msg = "    MeetAtNoon    "

# 1. Decode this message using the following steps:
# Step 1: Remove spaces, convert it lowercase.

cleaned_msg = msg.strip().lower()
print(cleaned_msg)

password = "123Password"

# How can we check that this password is alphanumeric ?
print(password.isalnum())


# Check if the string is palindrome or not

s = "level"

print(s.ljust(5) == "level")


# Question:
# Create a module designed for string modifications.
# Implement a few functions in the module.
# 1. normalize_text() --> String should be lowercase, without leading or trailing spaces.
# Replace multiple spaces with a single space.
# Example : "Name     is     Ashraf.    "  --> "name is ashraf."

# 2. extract_alpha_words(): Extract all the words which are only alphabets. Remove alphanumeric and digits.

# 3. remove_stopwords:
# ["is", "the", "and", "a", "an", "of"]

# 4. word_frequency:
# Return a dictionary where words are the keys and values are the frequencies.