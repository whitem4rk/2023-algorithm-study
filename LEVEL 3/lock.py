# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / 자물쇠와 열쇠

def rotate(key):
    return list(map(list, zip(*key[::-1])))

def check(lock, N):
    for i in range(N, N+N):
        for j in range(N, N+N):
                if lock[i][j] != 1: return False
    return True

def addkey(lock, key, row, col, M):
    for i in range(row, row+M):
        for j in range(col, col+M):
            lock[i][j] += key[i-row][j-col]
            
def subkey(lock, key, row, col, M):
    for i in range(row, row+M):
        for j in range(col, col+M):
            lock[i][j] -= key[i-row][j-col]

def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    new_lock = [[0 for _ in range(3*N)] for __ in range(3*N)]
    for i in range(N, N+N):
        for j in range(N, N+N):
                new_lock[i][j] = lock[i-N][j-N]
    
    # 자물쇠에 key를 더하고 모두 1이면 true 아니면 다시 key를 뻄
    for _ in range(4):
        key = rotate(key)
        for i in range(N+N+1):
            for j in range(N+N+1):
                addkey(new_lock, key, i, j, M)
                if check(new_lock, N):
                    return True
                else:
                    subkey(new_lock, key, i, j, M)
    
    return False



answer = True
my = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(my)
print('correct') if answer == my else print('wrong')