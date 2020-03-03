import heapq


def solution(jobs):
    jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    N = len(jobs)
    heap = []
    total = 0
    t = 0

    while True:
        # if there's no job and no queue
        if (not jobs) and (not heap):
            break
        # if there are jobs, take all jobs before t
        while jobs:
            if jobs[-1][0] <= t:
                heapq.heappush(heap, jobs.pop()[::-1])
            else:
                break
        # if queue is not empty, do the job in queue
        if heap:
            duration, in_time = heapq.heappop(heap)
            t += duration
            total += t - in_time
        # if queue is empty and there are jobs, jump to the first job start time
        else:
            t = jobs[-1][0]
    return total // N

'''
힙: []
t=0: 작업 확인. job의 t=0이라면 힙에 넣는다.
t=1~n-1: 작업중. 이 사이의 job 은 힙에 넣는다. 
t=n: 작업 확인.  ...

'''


if __name__ == '__main__':
    jobs = [[1, 8], [7, 1], [2, 6]]
    print(solution(jobs))