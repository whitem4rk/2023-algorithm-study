# 코딩테스트 연습 / 2021 카카오 채용연계형 인턴십 / 거리두기 확인하기

def is_safe(room:list, x:int, y:int) -> bool: # 북 동 남 서 순으로 진행
    one_step = [(-1,0),(0,1),(1,0),(0,-1)]
    two_step = [[(0,-1),(-1,0),(0,1)],[(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)]]
    
    # 결국 동서남북에서 P를 만나면 더 가지 않아도됨
    for i in range(len(one_step)):
        cur_x = x+one_step[i][0]
        cur_y = y+one_step[i][1]
        if 0 <= cur_x < 5 and 0 <= cur_y < 5:
            if room[cur_x][cur_y] == 'P':
                return False
            elif room[cur_x][cur_y] == 'O':
                for step2 in two_step[i]:
                    cur2_x = cur_x+step2[0]
                    cur2_y = cur_y+step2[1]
                    if 0 <= cur2_x < 5 and 0 <= cur2_y < 5:
                        if room[cur2_x][cur2_y] == 'P':
                            return False
    return True

def solution(places):
    answer = []
    
    for place in places:
        switch = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not is_safe(place, i, j):
                        switch = 0
                        break
        answer.append(switch)
        
    return answer

# test case 
answer = [1, 0, 1, 1, 1]
my_answer = solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

