# Input: The first line contains an integer, The  subsequent lines describe each student over  lines. First -> Name Second -> Scores
# Output: Prints os any student having the second lowest grade, order by names

if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        if score not in scores:
            scores.append(score)

    scores.sort()
    sorted_records = sorted(records, key = lambda x: (x[1], x[0]))
    second_low = 1
    
    for record in sorted_records:
        if record[1] == scores[second_low]:
            print(record[0])

