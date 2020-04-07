def solution(tickets):
    queue = [ticket for ticket in tickets if ticket[0] == 'ICN']

    answer = []
    while queue:
        path = queue.pop()
        if len(path) == len(tickets)+1:
            answer.append(path)

        remaining = [ticket for ticket in tickets]
        for i in range(len(path)-1):
            if path[i:i+2] in remaining:
                remaining.remove(path[i:i+2])

        for start, end in remaining:
            if start == path[-1]:
                queue.append(path + [end])
    return sorted(answer)[0]


# x1.5 faster
def solution2(tickets):
    answer = []
    stack = [[t] for t in tickets if t[0] == 'ICN']
    while stack:
        path = stack.pop()
        if len(path) == len(tickets):
            answer.append(path)

        remaining = [t for t in tickets]
        for t in path:
            if t in path:
                remaining.remove(t)

        while remaining:
            ticket = remaining.pop()
            if path[-1][-1] == ticket[0]:
                stack.append(path + [ticket])

    answer = sorted(answer)[0]
    answer = [a[0] for a in answer] + [answer[-1][-1]]
    return answer


if __name__ == '__main__':
    tickets1 = [['ICN', 'SFO'], ['SFO', 'ICN'], ['ICN', 'SFO'],['SFO', 'QRE']]
    tickets2 = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
    print(solution(tickets2))
