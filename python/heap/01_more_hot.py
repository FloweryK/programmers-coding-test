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


def solution2(scoville, K):
    heapq.heapify(scoville)
    trial = 0

    while True:
        if scoville[0] >= K:
            return trial
        if len(scoville) < 2:
            return -1
        else:
            trial += 1
            c1 = heapq.heappop(scoville)
            c2 = heapq.heappop(scoville)
            heapq.heappush(scoville, c1+c2*2)


if __name__ == '__main__':
    scoville = [1, 2, 3]
    K = 11
    print(solution(scoville, K))