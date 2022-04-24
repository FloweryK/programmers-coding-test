def solution(n, results):
    adj = [[0]*n for _ in range(n)]
    
    for i, j in results:
        adj[i-1][j-1] = 1
        adj[j-1][i-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not adj[i][j]:
                    if adj[i][k] * adj[k][j] == 1:
                        adj[i][j] = adj[i][k]
    
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if not adj[i][j]:
                count += 1
        if count == 1:
            answer += 1
    
    return answer


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))