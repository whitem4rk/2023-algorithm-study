# 코딩테스트 연습 / 2022 KAKAO TECH INTERNSHIP / 코딩 테스트 공부

def solution(alp:int, cop:int, problems:list) -> int:
    alp_target = max(list(zip(*problems))[0])
    cop_target = max(list(zip(*problems))[1])
    
    # 이미 목표치를 달성했다면
    if alp >= alp_target and cop >= cop_target:
        return 0
    
    # 마지막 return을 [alp_target][cop_target]으로 할것이기 떄문에 
    # alp > alp_target인 경우 alp_target = alp로 변경
    alp_target = max(alp_target,alp)
    cop_target = max(cop_target,cop)
    
    # 조건없이 가능한 학습
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    dp = [[float('inf')] * (cop_target+1) for _ in range(alp_target+1)]
    dp[alp][cop] = 0
    
    # (row, col) = (alp, cop)
    for row in range(alp, alp_target+1):
        for col in range(cop, cop_target+1):
            for prob in problems:
                cur_alp, cur_cop, plus_alp, plus_cop, cost = prob
                
                # alp, cop조건 미충족시
                if row < cur_alp or col < cur_cop:
                    continue
                
                # 다음 alp, cop가 out of range가 되지 않도록
                next_alp = min(alp_target, row+plus_alp)
                next_cop = min(cop_target, col+plus_cop)
                # cost가 더 작다면 갱신
                dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[row][col] + cost)
    
    return dp[alp_target][cop_target]

answer = 15
my = solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]])
print(my)
print('correct') if answer == my else print('wrong')