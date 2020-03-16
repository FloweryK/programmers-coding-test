def solution(begin, target, words):
    queue = [(begin, 0)]

    while queue:
        node = queue.pop()
        if target == node[0]:
            return node[1]

        if node[0] in words:
            words.remove(node[0])
        for word in words:
            sim = sum([int(c1==c2) for c1, c2 in zip(node[0], word)])
            if sim == len(word) - 1:
                queue.append((word, node[1]+1))
    return 0


# BFS solution
import queue


def solution2(begin, target, words):
    qu = queue.Queue()
    qu.put((0, begin))

    while qu.qsize() > 0:
        node = qu.get()

        if node[1] == target:
            return node[0]
        if node[1] in words:
            words.remove(node[1])

        for word in words:
            sim = sum([int(word[i] == node[1][i]) for i in range(len(word))])
            if sim == len(word) - 1:
                qu.put((node[0]+1, word))
    return 0


if __name__ == '__main__':
    begin = 'hit'
    target = 'hht'
    words = ['hhh', 'hht']
    print(solution(begin, target, words))
