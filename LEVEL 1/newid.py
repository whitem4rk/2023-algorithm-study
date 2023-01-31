# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 신규 아이디 추천

import re

def solution(new_id):
    answer = ''
    
    # phase 1
    process = new_id.lower()
    #phase 2
    process = re.sub('[^a-z0-9-_.]', '', process)
    #phase 3
    process = re.sub('\.\.+', '.', process)
    #phase 4
    process = re.sub('^\.|\.$', '', process)
    #phase 5
    if len(process) == 0:
        process = 'a' 
    #phase 6
    if len(process) >= 16:
        process = process[0:15]
        process = re.sub('\.$', '', process)
    #phase 7
    if len(process) <= 2:
        process = process.ljust(3, process[-1])
    answer = process
    return answer

# test case / answer = "bat.y.abcdefghi"
print(solution("...!@BaT#*..y.abcdefghijklm"))