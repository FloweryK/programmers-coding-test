def solution(numbers, target):
    answer = 0

    candidates = [0]
    for n in numbers:
        candidates = [c+n for c in candidates] + [c-n for c in candidates]
    
    for c in candidates:
        if c == target: answer += 1

    return answer


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))