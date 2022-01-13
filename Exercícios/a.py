if __name__ == '__main__':
    records = []
    temp = []
    for _ in range(int(input())):
        name = str(input())
        temp.append(name)
        score = float(input())
        temp.append(score)
        records.append(temp)
        temp.clear()

    print(records)