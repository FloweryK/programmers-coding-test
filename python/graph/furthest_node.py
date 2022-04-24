from collections import deque

def solution(n, edge):
    answer = 0
    
    # make adjacency matrix
    connected = [set() for _ in range(n)]
    for i,j in edge:
        connected[i-1].add(j-1)
        connected[j-1].add(i-1)
    
    # initialize stack and visited node
    visited = set()
    visited.add(0)
    
    q = deque()
    max_depth = 1
    for i in connected[0]:
        q.append((i, 1))    # node, depth
        visited.add(i)
    
    while q:
        i, depth = q.popleft()
        
        if depth == max_depth:
            answer += 1
        elif depth > max_depth:
            max_depth = depth
            answer = 1
        
        for j in connected[i]:
            if j not in visited:
                q.append((j, depth+1))
                visited.add(j)

    return answer


if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))