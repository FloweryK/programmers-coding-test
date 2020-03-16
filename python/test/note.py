# BFS solution
import queue


def solution(begin, target, words):
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
    target = 'cog'
    words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    print(solution(begin, target, words))


