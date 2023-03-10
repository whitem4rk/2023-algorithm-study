# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / 기둥과 보 설치

def check(case):
    for x, y, kind in case:
        if kind == 0:
            #'바닥 위' or '보의 한쪽 끝 위' or '또 다른 기둥 위' 
            if y == 0 or [x-1, y, 1] in case or [x, y, 1] in case or [x, y-1, 0] in case:
                continue
            return False
        elif kind == 1:
            #'한쪽 끝 부분이 기둥 위' or '양쪽 끝 부분이 다른 보와 동시 연결'
            if [x, y-1, 0] in case or [x+1, y-1, 0] in case or ([x-1, y, 1] in case and [x+1, y, 1] in case):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, kind, do = build
        if do == 1:
            answer.append([x, y, kind])
            if not check(answer): 
                answer.remove([x, y, kind])
        elif do == 0:
            answer.remove([x, y, kind])
            if not check(answer): 
                answer.append([x, y, kind])
    
    answer.sort()
    return answer


answer = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
my = solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print(my)
print('correct') if answer == my else print('wrong')

