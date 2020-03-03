def pp(matrix):
    for line in matrix:
        print(line)
    print('')


def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1

    for x in range(m):
        for y in range(n):
            if [x + 1, y + 1] in puddles:
                continue
            if ([x + 1, y] not in puddles) and y - 1 >= 0:
                dp[y][x] += dp[y - 1][x]
            if ([x, y + 1] not in puddles) and x - 1 >= 0:
                dp[y][x] += dp[y][x - 1]

    return dp[n-1][m-1] % 1000000007


if __name__ == '__main__':
    m = 4
    n = 3
    puddles = [[2, 2]]
    print(solution(m, n, puddles))