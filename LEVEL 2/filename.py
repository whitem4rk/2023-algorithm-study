# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] 파일명 정렬

import re

def solution(files):
    answer = []
    table = []
    # head/num/tail 구분후 배열저장
    for file in files:
        obj = re.search('\d+',file)
        head = file[:obj.start()]
        num = obj.group()
        tail = file[obj.end():]
        table.append([head,num,tail])
    # 정렬
    table.sort(key=lambda x: (x[0].lower(),int(x[1])))
    
    for file in table:
        answer.append(''.join(file))

    return answer

# test case 
answer = ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
my_answer = solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

