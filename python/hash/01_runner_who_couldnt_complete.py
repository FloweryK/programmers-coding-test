import collections


def solution(participant, completion):
    sol = collections.Counter(participant) - collections.Counter(completion)
    name = list(sol.keys())[0]
    return name


if __name__ == '__main__':
    participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
    completion = ['josipa', 'filipa', 'marina', 'nikola']
    print(solution(participant, completion))