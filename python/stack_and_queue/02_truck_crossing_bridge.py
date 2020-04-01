def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    crossing = [0] * bridge_length
    sec = 0

    while crossing:
        print(sec, crossing, truck_weights)
        sec += 1
        crossing.pop(0)

        if truck_weights:
            if sum(crossing) + truck_weights[-1] <= weight:
                crossing.append(truck_weights.pop())
            else:
                for i, c in enumerate(crossing):
                    if c:
                        crossing = crossing[i:] + [0] * (i+1)
                        sec += i
                        break
        else:
            for i, c in enumerate(crossing):
                if c:
                    crossing = crossing[i:]
                    sec += i
                    break
    return sec


if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))