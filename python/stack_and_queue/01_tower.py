from collections import deque


def solution2(heights):
    answer = [0] * len(heights)
    heights = [(i, heights[i]) for i in range(len(heights))]
    heights = deque(heights)

    while heights:
        i, height = heights.pop()
        for j in reversed(range(len(heights))):
            if heights[j][1] > height:
                answer[i] = j + 1
                break
    return answer


def solution(heights):
    heights = heights[::-1]
    signals = []
    answer = [0] * len(heights)

    for i_at, h_at in enumerate(heights):
        signals_copy = []
        for i_from, h_from in signals:
            if h_at > h_from:
                answer[i_from] = i_at
            else:
                signals_copy.append((i_from, h_from))
        signals_copy.append((i_at, h_at))
        signals = signals_copy

    answer = answer[::-1]
    for i in range(len(answer)):
        if answer[i]:
            answer[i] = len(answer) - answer[i]
    return answer


if __name__ == '__main__':
    heights = [6, 9, 5, 7, 4]
    print(solution2(heights))

