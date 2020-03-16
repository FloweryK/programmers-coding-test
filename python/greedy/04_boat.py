def solution(people, limit):
    boat = 0
    people = sorted(people, reverse=True)
    n = len(people)
    out = [0] * n

    while 0 in out:
        idx = out.index(0)
        for i in range(n-1, idx, -1):
            if (out[i] == 0) and (people[i] + people[idx] <= limit):
                out[i] = 1
                break
        out[idx] = 1
        boat += 1
    return boat


if __name__ == '__main__':
    people = [70, 50, 80]
    limit = 100
    print(solution(people, limit))