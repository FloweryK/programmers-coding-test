# https://programmers.co.kr/learn/courses/30/lessons/12907


def solution(n, money):
    money = sorted(money)
    # d[x][y]: money[0]~money[x] -> total y
    # d[x][y] = d[x-1][y] + d[x-1][y-money[x]] + d[x-1][y-2*money[x]] + ...
    # d[x][y] = d[x-1][y] + d[x][y-money[x]]

    d = [[0]*(n+1) for _ in range(len(money))]

    # first column
    for x in range(len(money)):
        d[x][0] = 1

    # first row
    for y in range(1, n+1):
        d[0][y] = 1 if y % money[0] == 0 else 0

    # rest elements
    for x in range(1, len(money)):
        for y in range(1, n+1):
            d[x][y] = d[x-1][y] + d[x][y-money[x]] * bool(y-money[x] >= 0)

    answer = d[-1][-1]
    return answer % 1000000007


if __name__ == '__main__':
    n = 5
    money = [1, 2, 5]
    print(solution(n, money))


