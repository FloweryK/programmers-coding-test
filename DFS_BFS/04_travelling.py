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


if __name__ == '__main__':
    tickets1 = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
    tickets2 = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
    print(solution(tickets2))
