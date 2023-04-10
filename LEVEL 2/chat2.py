# 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT / 오픈채팅방
# 실패 - 입력값 파싱 실패

def solution(record):
    userdict = {}
    for r in record:
        r = r.split()
        op, uid = r[0], r[1]
        if op == 'Enter' or op == 'Change':
            name = r[2]
            userdict[uid] = name
    
    answer = []
    for r in record:
        r = r.split()
        op, uid = r[0], r[1]
        if op == 'Enter':
            answer.append(f'{userdict[uid]}님이 들어왔습니다.')
        elif op == 'Leave':
            answer.append(f'{userdict[uid]}님이 나갔습니다.')
    
    return answer
    
        