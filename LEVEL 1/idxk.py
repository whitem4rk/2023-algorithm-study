# 코딩테스트 연습 / 정렬 / K번째수
# 실패 - 조건 누락 

def solution(array, commands):
    answer = []
    for com in commands:
        start, end, idx = com[0]-1, com[1], com[2]-1
        tmp = array[start:end]
        tmp.sort()
        answer.append(tmp[idx])
    return answer