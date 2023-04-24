# 코딩테스트 연습 / 탐욕법(Greedy) / 섬 연결하기
# 실패 - 쉬운 크루스칼 버젼

def solution(n, costs):
    costs.sort(key = lambda x:x[2])
    connected = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]
    while len(connected) != n:
        for i in range(1,len(costs)):
            a1, a2, cost = costs[i]
            if a1 in connected and a2 in connected:
                continue
            elif a1 in connected or a2 in connected:
                connected.add(a1)
                connected.add(a2)
                answer += cost
                break
    
    return answer