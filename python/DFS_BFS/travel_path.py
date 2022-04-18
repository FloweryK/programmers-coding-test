def solution(tickets):
    total = len(tickets)
    stack = [[t] for t in tickets if t[0] == 'ICN']
    candidates = []

    while stack:
        path = stack.pop()
        if len(path) == total:
            candidates.append(path)
        else:
            left = [t for t in tickets]
            for t in path:
                left.remove(t)
            
            for t in left:
                if path[-1][-1] == t[0]:
                    stack.append(path + [t])

    answer = sorted(candidates)[0]
    answer = [t[0] for t in answer] + [answer[-1][-1]]
    return answer


if __name__ == "__main__":
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    print(solution(tickets))