def solution(brown, red):
    for rows in range(1, int(red**0.5)+1):
        if red % rows == 0:
            columns = int(red / rows)
            if brown == 2 * (columns + rows) + 4:
                return sorted([columns+2, rows+2], reverse=True)


if __name__ == '__main__':
    brown = 24
    red = 24
    print(solution(brown, red))

    