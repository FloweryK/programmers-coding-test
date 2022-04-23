def solution(m, n, puddles):
    d = [[0]*(n+1) for _ in range(m+1)]
    p = [[0]*(n+1) for _ in range(m+1)]
    
    for i, j in puddles:
        p[i][j] = 1
    
    
    for j in range(1, n+1):
        for i in range(1, m+1):
            if i == 1 and j == 1:
                d[i][j] = 1
            elif p[i][j] == 1:
                continue
            else:
                d[i][j] = d[i-1][j] + d[i][j-1]
                
    return d[m][n] % 1000000007
            

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]

    print(solution(m, n, puddles))