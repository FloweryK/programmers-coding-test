import math


def solution(progresses, speeds):
    days_left = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]

    pivot = days_left[0]
    answer = [1]

    for day in days_left[1:]:
        if day <= pivot:
            answer[-1] += 1
        else:
            pivot = day
            answer.append(1)
    return answer


if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))
