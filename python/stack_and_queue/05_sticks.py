def solution(arrangement):
    arrangement = list(arrangement)
    stick = 0
    answer = 0

    while arrangement:
        braket = arrangement.pop()

        if braket == ')':
            if arrangement[-1] == '(':
                answer += stick
                _ = arrangement.pop()
            else:
                stick += 1
                answer += 1
        else:
            stick += -1

    return answer


if __name__ == '__main__':
    arrangement = '()(((()())(())()))(())'
    print(solution(arrangement))
