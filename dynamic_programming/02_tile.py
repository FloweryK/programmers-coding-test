def solution(N):
    size = [1, 1]
    for i in range(2, N):
        size.append(size[i-1] + size[i-2])
    return 2 * (2 * size[N-1] + size[N-2]) if N != 1 else 4


if __name__ == '__main__':
    N = 6
    print(solution(N))