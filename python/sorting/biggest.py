def solution(numbers):
    numbers = [str(n) for n in numbers]
    answer = ''.join(sorted(numbers, key=lambda x: (x*4)[:4], reverse=True))
    return str(int(answer))


if __name__ == "__main__":
    numbers = [6, 10, 2]
    print(solution(numbers))