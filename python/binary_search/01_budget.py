def solution(budgets, M):
    if sum(budgets) < M:
        return max(budgets)

    left = 1
    right = M
    mid = (left + right) // 2
    while left <= right:
        total = 0
        for b in budgets:
            total += b if b < mid else mid

        if total > M:
            right = mid - 1
        elif total < M:
            left = mid + 1
        mid = (right + left) // 2
    return mid


if __name__ == '__main__':
    budgets = [120, 110, 140, 150]
    M = 485
    print(solution(budgets, M))
