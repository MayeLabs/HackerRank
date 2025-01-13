# Input:The first line contains . The second line contains an array   of  integers each separated by a space.
# Output: return the second maximun number
# Example: [2, 3, 6, 6, 5 ], the maximun score is 6, second maximum is 6, second maximum is 5. we print 5 as the runner-up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = list(set(arr))
    score.sort(reverse=True)
    print(score[1])
