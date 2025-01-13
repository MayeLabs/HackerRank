# Questions for me
#-----------------
# What do they ask for ? : Aply split on a " ", to use join for delimeter, Exchange " " to -
# What do they give me ? :  A string
# What do I need ?: 
# Function split_and_join
# --->  Split for default use " "

def split_and_join(line):
    return("-".join(line.split()))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)