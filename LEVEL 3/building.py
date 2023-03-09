# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 파괴되지 않은 건물

# 손도 못 댄 문제 / 누적합이라는것을 모르는상태에서 풀 수 있을까?
def solution(board, skill):
    answer = 0
    sumboard = [ [0] * (len(board[0]) + 1) for _ in range(len(board)+1) ]    
    
    for op in skill:
        skill_type, r1, c1, r2, c2, degree = op
        degree = degree if skill_type == 2 else -degree
        
        sumboard[r1][c1] += degree
        sumboard[r2+1][c2+1] += degree
        sumboard[r1][c2+1] -= degree
        sumboard[r2+1][c1] -= degree
    
    for i in range(len(sumboard)):
        for j in range(1, len(sumboard[0])):
            sumboard[i][j] += sumboard[i][j-1] 
    
    for j in range(len(sumboard[0])):
        for i in range(1, len(sumboard)):
            sumboard[i][j] += sumboard[i-1][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += sumboard[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer


answer = 10
my = solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
print(my)
print('correct') if answer == my else print('wrong')

