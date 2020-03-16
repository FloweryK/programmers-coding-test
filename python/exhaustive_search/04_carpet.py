def solution(brown, red):
    for x in range(1, int(red**0.5)+1):
        if (red % x == 0) and (brown == 2*(x+red/x)+4):
            return sorted([x+2, red//x+2], reverse=True)


if __name__ == '__main__':
    brown = 24
    red = 24
    print(solution(brown, red))

    