def solution(numbers, target):
    l = [0]
    for n in numbers:
        l = [i+n for i in l] + [i-n for i in l]
    return l.count(target)


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))