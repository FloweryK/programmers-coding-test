def solution(number, k):
    answer = ''
    while k > 0:
        if k == len(number):
            number = ''
            break
        sub = [c for c in number[:k+1]]
        m = max(sub)
        answer += m
        number = number[sub.index(m)+1:]
        k += - sub.index(m)

    return answer + number



if __name__ == '__main__':
    number = '1924123'
    k = 6
    print(solution(number, k))