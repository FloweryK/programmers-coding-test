def solution(answers):
    result = [0, 0, 0]
    for i, answer in enumerate(answers):
        if [1, 2, 3, 4, 5][i % 5] == answer:
            result[0] += 1
        if [2, 1, 2, 3, 2, 4, 2, 5][i % 8] == answer:
            result[1] += 1
        if [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][i % 10] == answer:
            result[2] += 1
    answer = sorted([i+1 for i, score in enumerate(result) if score == max(result)])
    return answer


if __name__ == '__main__':
    answers = [1, 3, 2, 4, 2]
    print(solution(answers))