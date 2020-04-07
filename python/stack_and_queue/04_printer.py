def solution(priorities, location):
    waitings = [(i, p) for i, p in enumerate(priorities)]
    answer = 0

    while waitings:
        if waitings[0][1] < max([tup[1] for tup in waitings]):
            waitings.append(waitings.pop(0))
        else:
            answer += 1
            if waitings.pop(0)[0] == location:
                return answer


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))

