import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        s = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, s)
        answer += 1
    
    return answer


if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))