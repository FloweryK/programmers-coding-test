def solution(left, right):
    dp = [[0]*(len(right)+1) for _ in range(len(left)+1)]

    for i in range(len(left)):
        for j in range(len(right)):
            if left[i] > right[j]:
                dp[i][j] = max(dp[i][j-1] + right[j], dp[i-1][j-1], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
    return dp[len(left)-1][len(right)-1]


if __name__ == '__main__':
    left = [3, 2, 5]
    right = [2, 4, 1]
    print(solution(left, right))