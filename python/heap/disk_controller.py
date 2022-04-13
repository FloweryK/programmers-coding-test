import heapq

def solution(jobs):
    # 만약 q가 비어있으면
    ## 만약 jobs도 비어있으면 끝
    ## 만약 jobs가 있으면 q에 jobs를 던짐
    # 만약 q가 비어있지 않으면
    ## q를 interval 순으로 heapify
    ## q의 맨 앞 것을 꺼냄. 일 시작: t는 t_current + t_interval
    ## t_interval 앞에 있는 jobs들을 모두 q에 넣음
    
    answer = 0
    n = len(jobs)
    t_current = 0
    q = []

    jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    while jobs or q:
        if not q:
            i, t_interval = jobs.pop()
            t_current = i
            heapq.heappush(q, (t_interval, i))
        
        # 하나 꺼내서 일 시작
        t_interval, i = heapq.heappop(q)
        t_current += t_interval
        answer += t_current - i
        
        # 일하는 동안 들어온 작업들을 큐에 넣음
        while jobs and jobs[-1][0] <= t_current:
            i, t_interval = jobs.pop()
            heapq.heappush(q, (t_interval, i))
            
    
    return int(answer / n)


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6], [3, 5], [3, 7]]
    print(solution(jobs))