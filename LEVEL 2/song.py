# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] 방금그곡

# 소문자 변환 생각 못하고 정규식으로 해보려했으나 실패
def solution(m, musicinfos):
    answer = ''
    m = m.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
    
    score_list = []
    for info in musicinfos:
        info = info.split(',')
        h1, h2 = int(info[0][:2]), int(info[1][:2])
        m1, m2 = int(info[0][-2:])+h1*60, int(info[1][-2:])+h2*60
        # 시간길이
        t_len = m2 - m1
        
        # 악보 만들기
        tmp_str = ''
        info[3] = info[3].replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
        for i in range(t_len):
            tmp_str += info[3][i % len(info[3])]
        dup_m = m
        
        # 일치하는음이 있다면 저장
        if dup_m in tmp_str:
            score_list.append((len(dup_m), t_len, info[2]))
        
    if len(score_list) == 0:
        return '(None)'
    
    score_list.sort(key=lambda x: (-x[0],-x[1]))
    return score_list[0][2]

# test case 
answer = "WORLD"
my_answer = solution("DF",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

