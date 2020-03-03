import functools


def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    return str(int(''.join(numbers)))


def solution2(numbers):
    def __compare(a, b):
        t1 = int(a + b)
        t2 = int(b + a)
        return (t1 > t2) - (t1 < t2)

    numbers = [str(n) for n in numbers]
    numbers = sorted(numbers, key=functools.cmp_to_key(__compare), reverse=True)
    answer = str(int(''.join(numbers)))
    return answer


if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))

