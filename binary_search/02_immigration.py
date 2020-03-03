def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        total = sum([mid//t for t in times])
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == '__main__':
    n = 6
    times = [7, 10]
    print(solution(n, times))