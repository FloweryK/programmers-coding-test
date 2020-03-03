def solution(citations):
    citations = sorted(citations)

    for i, cite in enumerate(citations):
        h = len(citations) - i
        print(h)
        if h <= cite:
            return h
    return 0


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))