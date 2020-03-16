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


import queue

# BFS solution
def solution2(n, computers):
    answer = 0
    visited = [0]*n
    qu = queue.Queue()

    while 0 in visited:
        qu.put(visited.index(0))
        answer += 1

        while qu.qsize() > 0:
            i = qu.get()
            visited[i] = 1
            for j, connected in enumerate(computers[i]):
                if connected and (not visited[j]):
                    qu.put(j)
    return answer


if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))
