from itertools import permutations, combinations
from math import sqrt

'''def permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l'''


def is_prime(n):
    if n <= 1:
        return False
    for i in range(1, int(sqrt(n))):
        if n % (i + 1) == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    candidates = []
    for i in range(len(numbers)):
        for c in list(combinations(numbers, i+1)):
            for p in list(permutations(c)):
                n = int(''.join(p))
                if n not in candidates:
                    candidates.append(n)

    answer = 0
    for n in candidates:
        if is_prime(n):
            answer += 1
    return answer


if __name__ == '__main__':
    numbers = '011'
    print(solution(numbers))


