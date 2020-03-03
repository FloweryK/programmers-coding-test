from itertools import combinations


def solution(distance, rocks, n):
    min_dis = []

    for c in combinations(rocks, n):
        remaining = [rock for rock in rocks]
        for rock in c:
            del remaining[remaining.index(rock)]

        remaining = [0] + sorted(remaining) + [distance]
        dis = [remaining[i+1] - remaining[i] for i in range(len(remaining)-1)]
        min_dis.append(min(dis))

    return max(min_dis)


if __name__ == '__main__':
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2
    print(solution(distance, rocks, n))
