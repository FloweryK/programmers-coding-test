def solution(triangle):
    sumriangle = [[0]*len(line) for line in triangle]
    sumriangle[-1] = triangle[-1]

    for i in reversed(range(len(sumriangle)-1)):
        for j in range(i+1):
            sumriangle[i][j] = triangle[i][j] + max(sumriangle[i + 1][j], sumriangle[i + 1][j + 1])

    return sumriangle[0][0]


if __name__ == '__main__':
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))