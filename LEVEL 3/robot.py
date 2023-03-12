# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / 블록 이동하기

from collections import deque

def solution(board:list):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    visited = set()
    q = deque()
    q.append(((1,1),(1,2),0))

    while q:
        p1, p2, cnt = q.popleft()

        if (p1[0]+p2[0],p1[1]+p2[1]) in visited:
            continue
        # visited 확인은 점이 좌표가 2개이기 때문에 두 좌표의 합으로 표현
        visited.add((p1[0]+p2[0],p1[1]+p2[1]))
        
        if p1 == (n,n) or p2 == (n,n):
            return cnt
        
        # 가로 상태
        if p1[0] == p2[0]:
            #위 (위로 두칸이 0이라면 이동, 시계회전, 반시계회전 가능)
            if new_board[p1[0]-1][p1[1]] == 0 and new_board[p2[0]-1][p2[1]] == 0:
                q.append(((p1[0]-1,p1[1]), (p2[0]-1,p2[1]), cnt+1))
                q.append(((p1[0]-1,p1[1]), (p1[0],p1[1]), cnt+1))
                q.append(((p2[0],p2[1]), (p2[0]-1,p2[1]), cnt+1))
            #아래
            if new_board[p1[0]+1][p1[1]] == 0 and new_board[p2[0]+1][p2[1]] == 0:
                q.append(((p1[0]+1,p1[1]), (p2[0]+1,p2[1]), cnt+1))
                q.append(((p1[0]+1,p1[1]), (p1[0],p1[1]), cnt+1))
                q.append(((p2[0],p2[1]), (p2[0]+1,p2[1]), cnt+1))
            #오른쪽 (오른쪽 칸이 0이라면 이동)
            if new_board[p1[0]][p1[1]+1] == 0 and new_board[p1[0]][p2[1]+1] == 0:
                q.append(((p1[0],p1[1]+1), (p2[0],p2[1]+1), cnt+1))
            #왼쪽
            if new_board[p1[0]][p1[1]-1] == 0 and new_board[p1[0]][p2[1]-1] == 0:
                q.append(((p1[0],p1[1]-1), (p2[0],p2[1]-1), cnt+1))
        # 세로 상태
        else:
            #왼쪽
            if new_board[p1[0]][p1[1]-1] == 0 and new_board[p2[0]][p2[1]-1] == 0:
                q.append(((p1[0],p1[1]-1), (p2[0],p2[1]-1), cnt+1))
                q.append(((p1[0],p1[1]-1), (p1[0],p1[1]), cnt+1))
                q.append(((p2[0],p2[1]), (p2[0],p2[1]-1), cnt+1))
            #오른쪽
            if new_board[p1[0]][p1[1]+1] == 0 and new_board[p2[0]][p2[1]+1] == 0:
                q.append(((p1[0],p1[1]+1), (p2[0],p2[1]+1), cnt+1))
                q.append(((p1[0],p1[1]+1), (p1[0],p1[1]), cnt+1))
                q.append(((p2[0],p2[1]), (p2[0],p2[1]+1), cnt+1))
            #아래
            if new_board[p1[0]+1][p1[1]] == 0 and new_board[p2[0]+1][p2[1]] == 0:
                q.append(((p1[0]+1,p1[1]), (p2[0]+1,p2[1]), cnt+1))
            #위
            if new_board[p1[0]-1][p1[1]] == 0 and new_board[p2[0]-1][p2[1]] == 0:
                q.append(((p1[0]-1,p1[1]), (p2[0]-1,p2[1]), cnt+1))
        
answer = 7
my = solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
print(my)
print('correct') if answer == my else print('wrong')