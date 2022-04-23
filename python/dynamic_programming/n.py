def solution(N, number):
    d = [{int(str(N)*i)} for i in range(1, 9)]
    
    for i in range(1, 9):
        for j in range(1, i):
            for n in d[j-1]:
                for m in d[i-j-1]:
                    d[i-1].add(n+m)
                    d[i-1].add(n-m)
                    d[i-1].add(n*m)
                    if m: d[i-1].add(n//m)
        if number in d[i-1]:
            return i
    
    return -1


if __name__ == "__main__":
    N = 5
    number = 12
    print(solution(N, number))