def solution(n, lost, reserve):
    result = [l for l in lost]
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            result.remove(l)

    lost = result
    result = [l for l in lost]
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            result.remove(l)
        elif l+1 in reserve:
            reserve.remove(l+1)
            result.remove(l)
    return n - len(result)


if __name__ == '__main__':
    n = 8
    lost = [4, 5]
    reserve = [5, 6]
    print(solution(n, lost, reserve))