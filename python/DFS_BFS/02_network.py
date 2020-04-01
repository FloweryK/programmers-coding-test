# DFS solution
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

# DFS solution, x2 faster
def solution2(n, computers):
    networks = 0
    not_visited = [i for i in range(n)]

    while not_visited:
        networks += 1
        head = not_visited.pop()
        stack = []
        stack.append(head)

        while stack:
            tail = stack.pop()
            for i, connected in enumerate(computers[tail]):
                if connected and (i in not_visited):
                    stack.append(i)
                    not_visited.remove(i)
    return networks


# BFS solution
import queue
def solution3(n, computers):
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


# BFS solution, x3 faster
from collections import deque
def solution4(n, computers):
    networks = 0
    not_visited = [i for i in range(n)]

    while not_visited:
        networks += 1
        head = not_visited.pop()
        queue = deque()
        queue.append(head)

        while queue:
            tail = queue.popleft()
            for i, connected in enumerate(computers[tail]):
                if connected and (i in not_visited):
                    queue.append(i)
                    not_visited.remove(i)
    return networks


if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))
