# Input:The first line contains an integer. The second line contains the number for elements
# Output: Print the result of hash(t)


if __name__ == '__main__':
    n = int(input())
    elem_t = tuple(map(int, input().split()))
    print(hash(elem_t))
    