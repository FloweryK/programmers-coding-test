import collections

def solution(clothes):
    counter = collections.defaultdict(int)
    
    for _, kind in clothes:
        counter[kind] += 1
    
    answer = 1
    for count in counter.values():
        answer *= count + 1
    
    return answer - 1


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))