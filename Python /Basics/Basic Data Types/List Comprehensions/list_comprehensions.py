# Input: Four interger x,y,z each on a separate line
# Output: return a list with the permutation and remove all arrays that sum = n to leave valid permuts

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(lst)
