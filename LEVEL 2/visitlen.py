# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 방문 길이
# 실패 - 조건문 항상 신중히

dir = {'U':(0,1),'R':(1,0), 'D':(0,-1), 'L':(-1,0)}

def solution(dirs):
    answer = 0
    x, y = 5, 5
    path = set()
    
    for d in dirs:
        n_x, n_y = x+dir[d][0], y+dir[d][1]

        if not 0 <= n_x <= 10 or not 0 <= n_y <= 10:
            continue
        
        if (x,y,n_x,n_y) not in path and (n_x,n_y,x,y) not in path:
            path.add((x,y,n_x,n_y))
            answer += 1
        x, y = n_x, n_y         
    return answer