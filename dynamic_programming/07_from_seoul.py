def solution(K, travel):
    dp = [0] * 100001
    for i in range(len(travel)):
        for j in reversed(range(K+1)):
            dp[j] = -1
            if j >= travel[i][0]:
                dp[j] = max(dp[j], dp[j - travel[i][0]] + travel[i][1])
            if j >= travel[i][2]:
                dp[j] = max(dp[j], dp[j - travel[i][2]] + travel[i][3])
    return dp[K]


def solution2(K, travel):
    n = len(travel)
    d = [[0]*(K+1) for _ in range(n)]

    for i in range(n):
        w_time, w_money, b_time, b_money = travel[i]
        for time in range(K+1):
            walk = d[i-1][time-w_time] + w_money if (time >= w_time) and (d[i-1][time-w_time] != -1) else -1
            bike = d[i-1][time-b_time] + b_money if (time >= b_time) and (d[i-1][time-b_time] != -1) else -1
            d[i][time] = max(walk, bike)
    return d[-1][-1]



if __name__ == '__main__':
    K = 1650
    travel = [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]
    print(solution2(K, travel))

