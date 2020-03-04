def solution(n, times):
    left = 1
    right = n*max(times)
    mid = (left + right) // 2

    while left <= right:
        available = sum([mid//t for t in times])
        if available > n:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return mid


if __name__ == '__main__':
    n = 6
    times = [7, 10]
    print(solution(n, times))