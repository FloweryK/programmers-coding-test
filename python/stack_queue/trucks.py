from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    on_bridge = deque([])
    current_weight = 0

    t = 0
    
    while truck_weights or on_bridge:
        for i in range(len(on_bridge)):
            on_bridge[i][1] += 1
        
        if on_bridge and on_bridge[0][1] >= bridge_length:
            w = on_bridge.popleft()[0]
            current_weight -= w
        
        if truck_weights and weight >= truck_weights[0] + current_weight:
            w = truck_weights.popleft()
            on_bridge.append([w, 0])
            current_weight += w
        elif on_bridge:
            jump = bridge_length - on_bridge[0][1] - 1
            for i in range(len(on_bridge)):
                on_bridge[i][1] += jump
            t += jump
        
        t += 1
    
    return t


if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    print(solution(bridge_length, weight, truck_weights))