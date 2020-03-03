import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    mix = 0
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return mix
        else:
            mix += 1
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + 2 * b)
    if scoville[0] >= K:
        return mix
    else:
        return -1


if __name__ == '__main__':
    scoville = [1, 2, 3]
    K = 11
    print(solution(scoville, K))