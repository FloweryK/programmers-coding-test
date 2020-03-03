def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)

    start = 1
    end = M
    cut = (start+end)//2
    while end-start != 1:
        total = 0
        for b in budgets:
            total += b if b < cut else cut

        if total > M:
            end = cut
        else:
            start = cut
        cut = (start + end) // 2
    return cut


if __name__ == '__main__':
    budgets = [120, 110, 140, 150]
    M = 485
    print(solution(budgets, M))
