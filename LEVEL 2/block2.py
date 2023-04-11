# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 프렌즈4블록
# 실패 - 인덱스 관리 개판 ㅠ

def solution(m, n, board):
    nboard = [[] * m for _ in range(n)]
            
    for i in range(n):
        for j in reversed(range(m)):
            nboard[i].append(board[j][i])
            
    cnt = 0
    while True: 
        delset = set()
        for i in range(n-1):
            for j in range(m-1):
                if nboard[i][j] != '0' and nboard[i][j+1] != '0' and nboard[i+1][j] != '0' and nboard[i+1][j+1] != '0':
                    if nboard[i][j] == nboard[i][j+1] == nboard[i+1][j] == nboard[i+1][j+1]:
                        delset.add((i,j))
                        delset.add((i,j+1))
                        delset.add((i+1,j))
                        delset.add((i+1,j+1))
        
        if len(delset) == 0:
            return cnt
        
        delset = sorted(delset, key=lambda x: (-x[1]))
        cnt += len(delset)
        
        for i,j in delset:
            nboard[i].pop(j)
            nboard[i].append('0')