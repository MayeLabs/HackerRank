# Input: int n 1 <= n <= 20
# Output: Print n lines, one corresponding to each i
# Example:
# 5 -> 0 1 4 9 16

if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        print (i**2)
        
