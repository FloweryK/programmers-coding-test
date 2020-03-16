def solution(N, number):
    s = [{int(str(N)*i)} for i in range(1, 9)]

    for i in range(8):
        for j in range(i):
            for ni in s[j]:
                for nj in s[i-j-1]:
                    s[i].add(ni+nj)
                    s[i].add(ni-nj)
                    s[i].add(ni*nj)
                    if nj:
                        s[i].add(ni // nj)
        if number in s[i]:
            return i+1
    return -1


if __name__ == '__main__':
    N = 5
    number = 12
    print(solution(N, number))
