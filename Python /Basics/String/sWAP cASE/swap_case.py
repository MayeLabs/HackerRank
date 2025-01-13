# Questions for me
#-----------------
# What do they ask for ? : They need that by a string, I convert from upper to lower, and from lower to upper -> Example HoLa = hOlA   
# What do they give me ? :  A string
# What do I need ?: 
# Function swap_case
# Function of string for converting and identification 
# For because I need iterate trough the array

""" Before Function
def swap_case(s):
    word = ''
    for i in range(len(s)):
        if s[i].islower():
            word = word + s[i].upper()
        else:
            word = word + s[i].lower()
    return word
"""

# Best Function
def swap_case(s):
    return ''.join([char.upper() if char.islower() else char.lower() for char in s])



if __name__ == '__main__':
    word = input()
    print(swap_case(word))


# Why is better ? 
# Concatenate can be expensive, because each time that concatenate python create a new string the join of list is more efficient
# The best of way to read a str is using only input 