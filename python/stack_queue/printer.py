from collections import deque

def solution(priorities, location):
    answer = 0

    p_sorted = sorted(priorities)
    priorities = deque([(p, i) for i, p in enumerate(priorities)])

    while True:
        p, i = priorities.popleft()

        if p == p_sorted[-1]:
            p_sorted.pop()
            answer += 1

            if i == location:
                break
        else:
            priorities.append((p, i))

    return answer


if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))