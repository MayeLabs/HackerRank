# Input: int n
# Output: List od integers from 1 through n as a string without spaces
# Example: 3 -> 123

if __name__ == '__main__':
    n = int(input())
    secu = '' 
    for i in range(1,n+1):
        secu = secu + str(i)
    print(secu)
