if __name__ == '__main__':
    na = []
    sc = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        na.append(name)
        sc.append(score)
    s = sorted(zip(sc,na))
    get_min = sorted(list(set(sc)))[1]
    for num in s:
        if(num[0]==get_min):
            print(num[1])