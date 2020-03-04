import heapq


def solution(operations):
    queue = []
    for op in operations:
        if op[0] == 'I':
            heapq.heappush(queue, int(op[2:]))
        if queue:
            if op == 'D -1':
                _ = heapq.heappop(queue)
            elif op == 'D 1':
                queue = [-q for q in queue]
                heapq.heapify(queue)
                _ = heapq.heappop(queue)
                queue = [-q for q in queue]
                heapq.heapify(queue)
    if queue:
        return [max(queue), min(queue)]
    else:
        return [0, 0]


if __name__ == '__main__':
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))
