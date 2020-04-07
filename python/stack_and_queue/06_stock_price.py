

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1

            if prices[i] > prices[j]:
                break
    return answer


from collections import deque
def solution2(prices):
    answer = []
    prices = deque(prices)

    while prices:
        p = prices.popleft()
        count = 0

        for pp in prices:
            count += 1
            if p > pp:
                break
        answer.append(count)
    return answer



if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))

