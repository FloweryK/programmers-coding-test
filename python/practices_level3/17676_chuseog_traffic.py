# https://programmers.co.kr/learn/courses/30/lessons/17676
import datetime


def solution(lines):
    logs = []
    for line in lines:
        line = line.split(' ')
        duration = float(line[2][:-1]) * 1000 - 1
        end = datetime.datetime.strptime(line[0] + ' ' + line[1], '%Y-%m-%d %H:%M:%S.%f')
        start = end - datetime.timedelta(milliseconds=duration)
        logs.append((start, end))
    logs = sorted(logs, key=lambda x: x[0], reverse=True)

    max = -1
    for log in logs:
        for right in log:
            num = 0
            left = right - datetime.timedelta(milliseconds=999)
            for start, end in logs:
                if not ((right < start) or (end < left)):
                    num += 1

            if num > max:
                max = num
    return max


if __name__ == '__main__':
    lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
    print(solution(lines))
