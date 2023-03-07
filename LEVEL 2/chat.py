# 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT / 오픈채팅방

def solution(record):
    answer = []
    nick_dict = {}
    
    for rec in record:
        if len(rec.split(' ')) == 3:
            state, uid, name = rec.split(' ')
            nick_dict[uid] = name
            
    for rec in record:
        state, uid, = rec.split(' ')[0], rec.split(' ')[1]
        
        if state == 'Enter':
            answer.append(nick_dict[uid]+'님이 들어왔습니다.')
        elif state == 'Leave':
            answer.append(nick_dict[uid]+'님이 나갔습니다.')
    
    return answer

# test case
answer = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
my_answer = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(my_answer)
if answer == my_answer:
    print('correct!')
else:
    print('wrong')
    
