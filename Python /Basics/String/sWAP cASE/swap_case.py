# Questions for me
#-----------------
# What do they ask for ? : They need that by a string, I convert from upper to lower, and from lower to upper -> Example HoLa = hOlA   
# What do they give me ? :  A string
# What do I need ?: 
# Function swap_case
# Function of string for converting and identification 
# For because I need iterate trough the array

def swap_case(s):
    word = ''
    for i in range(len(s)):
        if s[i].islower():
            word = word + s[i].upper()
        else:
            word = word + s[i].lower()
    return word


if __name__ == '__main__':
    word = str(input())
    print(swap_case(word))

