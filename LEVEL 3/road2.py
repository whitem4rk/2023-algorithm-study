from collections import deque
# 동 남 서 북
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def solution(board):
    n = len(board)
    dp = [[[float('inf')] * (n+2) for _ in range(n+2)] for _ in range(4)]
    lap = [[1] * (n+2) for _ in range(n+2)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            lap[i+1][j+1] = board[i][j]

    q = deque([[1, 2, 0, 100], [2, 1, 1, 100]])
    dp[0][1][1] = 0
    dp[1][1][1] = 0
    dp[2][1][1] = 0
    dp[3][1][1] = 0

    while q:
        cur_r, cur_c, cur_dir, cur_cost = q.popleft()
        if lap[cur_r][cur_c] == 1:
            continue
        if dp[cur_dir][cur_r][cur_c] < cur_cost:
            continue
        dp[cur_dir][cur_r][cur_c] = cur_cost

        for idx, d in enumerate(dir):
            next_r, next_c = cur_r + d[0], cur_c + d[1]
            if lap[next_r][next_c] == 1:
                continue
            if idx == cur_dir:
                q.append([next_r, next_c, idx, cur_cost + 100])
            else:
                q.append([next_r, next_c, idx, cur_cost + 600])
    answer = [dp[i][n][n] for i in range(len(dp))]
    return min(answer)
