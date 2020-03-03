import heapq


def solution(operations):
    heap = []
    for op in operations:
        if op[0] == 'I':
            heapq.heappush(heap, int(op[2:]))
        else:
            if heap:
                if op[2:] == '-1':
                    _ = heapq.heappop(heap)
                else:
                    heap = [-x for x in heap]
                    heapq.heapify(heap)
                    _ = heapq.heappop(heap)
                    heap = [-x for x in heap]
                    heapq.heapify(heap)
    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]


if __name__ == '__main__':
    operations = ['I 16', 'D 1']
    print(solution(operations))
