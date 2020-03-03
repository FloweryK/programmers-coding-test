import collections


def solution(clothes):
    counter = collections.Counter([c[1] for c in clothes])
    answer = 1
    for key, value in counter.items():
        answer *= (value + 1)
    return answer - 1


if __name__ == '__main__':
    clothes = [['yellow_hat', 'headgear'],
               ['blue_sunglasses', 'eyewear'],
               ['green_turban', 'headgear']]
    print(solution(clothes))