def solution(n, computers):
    answer = 0
    visited = [0] * n
    stack = []

    while 0 in visited:
        stack.append(visited.index(0))
        answer += 1
        while stack:
            i = stack.pop()
            visited[i] = 1

            for j, connection in enumerate(computers[i]):
                if connection and not visited[j]:
                    stack.append(j)
    return answer


if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))
