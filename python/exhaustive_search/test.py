def solution(answers):
    c1, c2, c3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == [1, 2, 3, 4, 5][i % 5]:
            c1 += 1
        if answers[i] == [2, 1, 2, 3, 2, 4, 2, 5][i % 8]:
            c2 += 1
        if answers[i] == [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][i % 10]:
            c3 += 1
    
    m = max([c1, c2, c3])
    answer = sorted([i+1 for i, c in enumerate([c1, c2, c3]) if c == m])
    
    return answer


if __name__ == "__main__":
    answers = [1, 2, 3, 4, 5]
    print(solution(answers))