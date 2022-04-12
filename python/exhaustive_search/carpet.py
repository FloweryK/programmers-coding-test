def solution(brown, yellow):
    total = brown + yellow

    for h in range(3, int(total ** 0.5) + 1):
        if (total % h == 0) and ((h-2)*(total//h-2) == yellow):
            return [total//h, h]


if __name__ == "__main__":
    brown = 10
    yellow = 2
    print(solution(brown, yellow))