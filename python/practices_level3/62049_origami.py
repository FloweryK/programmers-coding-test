# https://programmers.co.kr/learn/courses/30/lessons/62049


def solution(n):
    answer = [0] * (2**n - 1)
    for i in range(2, n+1):
        answer[2**(i-1)-1] = 0
        for j in range(2**(i-1), 2**i-1):
            answer[j] = (answer[2**i-2-j] + 1) % 2
    return answer


def solution2(n):
    answer = [0]
    for i in range(n-1):
        answer = answer + [0] + [a^1 for a in reversed(answer)]
    return answer


if __name__ == '__main__':
    n = 3
    print(solution2(n))
