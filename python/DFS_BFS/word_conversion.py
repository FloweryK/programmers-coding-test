from collections import deque

def solution(begin, target, words):
    q = deque([[begin]])

    while q:
        path = q.popleft()

        left = [word for word in words if word not in path]

        for word in left:
            dis = sum(int(c1 != c2) for c1, c2 in zip(word, path[-1]))

            if dis == 1:
                if word == target:
                    return len(path)
                else:
                    q.append(path + [word])

    return 0
    

if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))