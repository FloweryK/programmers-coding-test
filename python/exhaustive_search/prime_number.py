import math
from itertools import permutations

cache = {}

def is_prime(n):
    try:
        return cache[n]
    except:
        if n < 2:
            cache[n] = False
            return False

        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                cache[n] = False
                return False
        cache[n] = True
        return True


def solution(numbers):
    numbers = list(numbers)
    
    answer = 0
    candidates = {int(''.join(p)) for i in range(1, len(numbers)+1) for p in permutations(numbers, i) }
    for n in candidates:
        if is_prime(n):
            answer += 1
    
    return answer


if __name__ == "__main__":
    numbers = "011"
    print(solution(numbers))