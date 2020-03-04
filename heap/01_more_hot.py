import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    mix = 0
    while (len(scoville) > 1) and scoville[0] < K:
        mix += 1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 + 2 * s2)

    if scoville[0] < K:
        return -1
    else:
        return mix


if __name__ == '__main__':
    scoville = [1, 2, 3]
    K = 11
    print(solution(scoville, K))