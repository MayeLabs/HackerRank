if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):

        command = [int(x) if x.isdigit() else x.lower() for x in input().split(" ")]

        if 'insert' in command:
            lst.insert(int(command[1]), command[2])

        elif 'print' in command:
            print(lst)

        elif 'remove' in command:
            lst.remove(command[1])

        elif 'append' in command:
            lst.append(command[1])

        elif 'sort' in command:
            lst.sort()

        elif 'pop' in command:
            lst.pop()
            
        elif 'reverse' in command:
            lst.reverse()