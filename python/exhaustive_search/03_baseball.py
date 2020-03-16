from itertools import combinations, permutations


def solution(baseball):
    candidates = []
    for c in combinations(range(1, 10), 3):
        for p in permutations(c):
            candidates.append(100*p[0]+10*p[1]+p[2])

    for guess, strike, ball in baseball:
        new_candidates = []
        for c in candidates:
            guess = str(guess)
            c = str(c)
            s = int(guess[0] == c[0]) + int(guess[1] == c[1]) + int(guess[2] == c[2])
            b = c.count(guess[0]) + c.count(guess[1]) + c.count(guess[2]) - strike
            if (strike == s) and (ball == b):
                new_candidates.append(c)
        candidates = new_candidates

    answer = len(candidates)
    return answer


if __name__ == '__main__':
    baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
    print(solution(baseball))

