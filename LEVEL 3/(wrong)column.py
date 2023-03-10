# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / 기둥과 보 설치


# 로직은 맞는거 같은데 자꾸 런타임에러가 뜬다. 끙끙대다가 결국 포기...
def bo_check(board:list, x:int, y:int) -> bool:
    if (0 in board[x][y-1] or 0 in board[x+1][y-1]) or (0<x and (1 in board[x-1][y] and 1 in board[x+1][y])):
        return True
    return False

def col_check(board:list, x:int, y:int) -> bool:
    if y==0 or (x>0 and ((1 in board[x-1][y]) or (1 in board[x][y]))) or (y>0 and (0 in board[x][y-1])):
        return True
    return False

def create(board:list, x:int, y:int, kind:int, answer:list):
    # 기둥 설치
    if kind == 0:
        if col_check(board, x, y):
            board[x][y].append(0)
            answer.append([x,y,kind])
    # 보 설치
    if kind == 1:
        if bo_check(board, x, y):
            board[x][y].append(1)
            answer.append([x,y,kind])
 
def delete(board:list, x:int, y:int, kind:int, answer:list):
    # 제거하고 나머지가 다 조건을 만족하는지 확인
    board[x][y].remove(kind)
    answer.remove([x,y,kind])
    for case in answer:
        _x, _y, _kind = case
        if (_kind == 0 and not col_check(board, _x, _y)) or (_kind == 1 and not bo_check(board, _x, _y)):
            board[x][y].append(kind)
            answer.append([x,y,kind])
            return
 
def solution(n, build_frame):
    answer = []
    board = [ [ [] * (n+1) for _ in range(n+1) ] for _ in range(n+1) ]
    for build in build_frame:
        x, y, kind, do = build
        if do == 0:
            delete(board,x,y, kind, answer)
        elif do == 1:
            create(board,x,y, kind, answer)
    
    answer.sort()
    return answer


answer = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
my = solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print(my)
print('correct') if answer == my else print('wrong')

