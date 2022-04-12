import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        jump = math.ceil((100 - progresses[0]) / speeds[0])
        for i in range(len(progresses)):
            progresses[i] += jump * speeds[i]
        
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        answer.append(count)
    
    return answer


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]

    print(solution(progresses, speeds))