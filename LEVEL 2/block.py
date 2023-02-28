# 코딩테스트 연습/ 2018 KAKAO BLIND RECRUITMENT / [1차] 프렌즈4블록

from collections import deque

def solution(m, n, board):
    answer = 0
    # 터졌을때 col 기준으로 나머지가 내려가기 떄문에 row, col을 바꿔준다.
    colrow_board = deque(map(deque, zip(*board)))

    while True: 
        del_point = set()
        # 4칸씩 체크하면서 터트릴것이 있다면 set에 넣기
        for i in range(0, n-1):
            for j in range(0, m-1):
                cur = colrow_board[i][j] 
                if cur != 'X' and cur == colrow_board[i][j+1] and cur == colrow_board[i+1][j] and cur == colrow_board[i+1][j+1]:
                    del_point.add((i,j))
                    del_point.add((i,j+1))
                    del_point.add((i+1,j))
                    del_point.add((i+1,j+1))
        # 위에 위치하는것부터 터트려야하므로 정렬
        del_point = sorted(del_point,key=lambda x: (x[1],x[0]))
        
        # 만약 지울것이 없다면 
        if len(del_point) == 0:
            break
        
        # 터트린후에 X로 배열 맨 앞에 넣어주기
        for point in del_point:
            row, col = point
            del colrow_board[row][col]
            answer += 1
            colrow_board[row].appendleft('X')
        
    return answer

# test case
answer = 15
my_answer = solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
print(my_answer)
print('correct') if answer == my_answer else print('wrong')
