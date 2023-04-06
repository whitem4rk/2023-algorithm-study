# 코딩테스트 연습 / 스택/큐 / 기능개발
# 실패

def solution(progresses, speeds):
    answer = []
    sec = 0
    idx = 0
    cur_sum = 0
    
    while True:
        if idx == len(progresses):
            answer.append(cur_sum)
            break
        
        if progresses[idx] + (speeds[idx] * sec) >= 100:
            cur_sum += 1
            idx += 1
        else:
            if cur_sum != 0:
                answer.append(cur_sum)
            cur_sum = 0
            sec += 1
    
    return answer