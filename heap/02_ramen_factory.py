import heapq


def solution(stock, dates, supplies, k):
    lst = [(d, s) for d, s in zip(dates, supplies)]
    lst = sorted(lst, key=lambda x: x[1], reverse=True)

    day = 0
    day += stock
    supply = 0

    while day < k:
        for i in range(len(lst)):
            if lst[i][0] <= day:
                supply += 1
                day += lst[i][1]
                del lst[i]
                break
    return supply


def solution2(stock, dates, supplies, k):
    heap = [(-s, s, d) for s, d in zip(supplies, dates)]
    heapq.heapify(heap)

    day = 0
    answer = 0

    while day < k:
        stock += -1
        if stock < 0:
            future = []
            while True:
                h = heapq.heappop(heap)
                if h[2] > day:
                    future.append(h)
                else:
                    stock += h[1]
                    for h in future:
                        heapq.heappush(heap, h)
                    answer += 1
                    break
        day += 1
    return answer


if __name__ == '__main__':
    stock = 4
    dates = [4, 10, 15]
    supplies = [20, 5, 10]
    k = 30
    print(solution(stock, dates, supplies, k))