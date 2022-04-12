def solution(prices):
    answer = [0] * len(prices)
    stack = [0]

    for i in range(1, len(prices)):
        print(answer, stack)
        # 만약 방금 전 price가 현 price보다 더 크면
        if prices[stack[-1]] > prices[i]:
            # 시간을 거꾸로 돌아가면서
            for j in stack[::-1]:
                # 만약 현 price보다 큰 price가 있으면
                if prices[i] < prices[j]:
                    # 그 price는 이제 가격이 더 떨어진 지점을 찾았다.
                    answer[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    
    # 아직도 스택에 남아있는게 있으면
    for i in range(len(stack)-1):
        # 그건 떨어진 지점이 없는거임
        # 근데 맨 마지막꺼는 어차피 0이니까 건들지말자
        answer[stack[i]] = len(prices) - stack[i] - 1
    
    return answer
