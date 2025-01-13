#Input:  dictionary containing key/value pairs of name:[marks] for a list of students. 
#Output: The average of the marks obtained by the particular student correct to 2 decimal places.
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0
    for elem in student_marks[query_name]:
        sum+=elem
    avg = sum/len(student_marks[query_name])
    print("{:.2f}".format(avg))