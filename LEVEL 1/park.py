# 코딩테스트 연습 / 연습문제 / 공원 산책
# 성공

direction = {"E":(0, 1), "W":(0, -1), "N":(-1, 0), "S":(1, 0)}

def solution(park, routes):
    answer = []
    cur = [0,0]
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                cur = [i, j]
    
    for route in routes:
        dir, cnt = route.split()
        cnt = int(cnt)
        
        tmp = cur.copy()
        for _ in range(cnt):
            tmp[0] += direction[dir][0]
            tmp[1] += direction[dir][1]
            if (tmp[0] == -1 or tmp[0] == len(park)) or (tmp[1] == -1 or tmp[1] == len(park[0])) or park[tmp[0]][tmp[1]] == 'X':
                tmp = cur
                break
        cur = tmp
    
        
    return cur