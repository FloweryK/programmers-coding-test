def solution(citations):
    citations = sorted(citations)

    for i, c in enumerate(citations):
        h = len(citations) - i

        if h <= c:
            return h
    return 0

if __name__ == "__main__":
    citations = [1, 4, 5, 6]
    print(solution(citations))