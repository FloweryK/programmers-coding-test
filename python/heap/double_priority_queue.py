import heapq

def solution(operations):
    q = []

    for op in operations:
        if op == "D 1":
            q = [-n for n in q]
            heapq.heapify(q)
            heapq.heappop(q)
            q = [-n for n in q]
        elif op == "D -1":
            heapq.heappop(q)
        else:
            n = int(op[2:])
            heapq.heappush(q, n)
    
    if q:
        mq = [-n for n in q]
        heapq.heapify(mq)
        maximum = -heapq.heappop(mq)
        minimum = heapq.heappop(q)
        return [maximum, minimum]
    else:
        return [0, 0]


if __name__ == "__main__":
    operations = ["I 16","D 1"]
    print(solution(operations))