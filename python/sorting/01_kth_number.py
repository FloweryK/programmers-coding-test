def solution(array, commands):
    answer = []

    for cmd in commands:
        start = cmd[0] - 1
        end = cmd[1] - 1
        k = cmd[2] - 1

        answer.append(sorted(array[start:end+1])[k])

    return answer


def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))

