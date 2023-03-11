# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 양과 늑대

# 풀이를 봐도 모르겠다... 도와주세요
def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = 0

	# 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    return max(answer)


answer = 5
my = solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])
print(my)
print('correct') if answer == my else print('wrong')

