import heapq


def solution(stock, dates, supplies, k):
    lst = sorted([(s, d) for s, d in zip(supplies, dates)], key=lambda x: x[0], reverse=True)

    day = 0
    answer = 0
    while day < k:
        stock += -1
        print('day %i stock %i' % (day, stock))
        if stock < 0:
            for i, (supply, date) in enumerate(lst):
                if date <= day:
                    stock += supply
                    answer += 1
                    break
            del lst[i]
        day += stock + 1
        stock = 0
    return answer


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