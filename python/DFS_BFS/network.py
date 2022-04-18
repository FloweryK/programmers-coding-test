def solution(n, computers):
    answer = 0
    visited = [False] * n

    # 만약 visited를 stack으로 관리하면 element를 삭제할 때 O(n)의 cost가 들어감.
    # 그래서 더 빠르게 삭제하기 위해 set을 사용
    left = {i for i in range(n)}  
    stack = []

    while left or stack:
        if not stack:
            answer += 1
            i = left.pop()
        else:
            i = stack.pop()
        
        visited[i] = True

        for j in range(n):
            if computers[i][j] and not visited[j]:
                visited[j] = True
                left.remove(j)
                stack.append(j)
        
    return answer


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

    print(solution(n, computers))