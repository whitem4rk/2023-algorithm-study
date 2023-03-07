# 코딩테스트 연습 / 2020 카카오 인턴십 / 경주로 건설

from collections import deque

direction = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(board):
    # board에 방향 차원을 더해서 현재 방향,비용을 저장해가면서 마지막 도착지점에 min(4방향)을 구함
    distance_map = [[[float('inf')] * len(board) for _ in range(len(board))] for __ in range(4)]
    for i in range(4):
        distance_map[i][0][0] = 0 
    q = deque()
    q.append((0,0,0,0))
    q.append((0,0,0,1))
    # 1,2,3,4  / 동남서북
    while q:
        row, col, fee, dir_idx = q.popleft()
        for idx in range(len(direction)):
            next_row = row + direction[idx][0]
            next_col = col + direction[idx][1]
            # 가려는곳의 범위, 벽 확인
            if 0 <= next_row < len(board) and 0 <= next_col < len(board) and board[next_row][next_col] == 0:
                cost = fee + 100 if direction[idx] == direction[dir_idx] else fee + 600
                if distance_map[idx][next_row][next_col] > cost:
                    distance_map[idx][next_row][next_col] = cost
                    q.append((next_row,next_col,cost,idx))
    last = [ distance_map[i][-1][-1] for i in range(4)]
    return min(last)

def solution(board):
    return bfs(board)



answer = 3200
my = solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])
print(my)
print('correct') if answer == my else print('wrong')