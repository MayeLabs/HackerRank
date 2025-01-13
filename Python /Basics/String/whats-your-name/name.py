# Questions for me
#-----------------
# What do they ask for ? : Complete the function print_full_name  replacing firstname and lastname for first and last 
# What do they give me ? :  2 string, The first and last name
# What do I need ?: 
# Concatenate first and last using + in of the print


def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")
    # Other Way
    #print(f"Hello {first} {last}! You just delved into python.")


    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)