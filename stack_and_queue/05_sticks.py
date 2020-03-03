def solution(arrangement):
    stack = []
    braket = []

    for i, char in enumerate(arrangement):
        if char == '(':
            stack.append([i, '('])
        else:
            braket.append((stack[-1][0], i))
            del stack[-1]

    laser = []
    stick = []
    for tup in braket:
        if tup[0] == (tup[1] - 1):
            laser.append(tup)
        else:
            stick.append(tup)

    cut = 0
    for s in stick:
        cut += 1
        for l in laser:
            if s[0] < l[0] < s[1]:
                cut += 1
    return cut


if __name__ == '__main__':
    arrangement = '(())'
    print(solution(arrangement))