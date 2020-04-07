from collections import deque


def solution(begin, target, words):
    queue = deque([[begin]])

    while queue:
        path = queue.popleft()
        print(path)
        if path[-1] == target:
            return len(path)-1

        remaining = [word for word in words if word not in path]
        while remaining:
            word = remaining.pop()
            sim = sum([int(c1 == c2) for c1, c2 in zip(word, path[-1])])
            if sim == len(word)-1:
                queue.append(path + [word])
    return 0


if __name__ == '__main__':
    begin = 'hit'
    target = 'cog'
    words = ['hhh', 'hht']
    print(solution(begin, target, words))
