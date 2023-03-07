# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 메뉴 리뉴얼

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 모든 주문마다 course 개수만큼의 조합을 만든후에
    for cour in course:
        tmp_list = []
        for order in orders:
            comb = list(combinations(sorted(order), cour))
            tmp_list.extend(comb)
        
        # Counter로 빈도수 저장
        cnt = Counter(tmp_list)
        max_val = 0
        
        # 가장 많이 나온 메뉴가 k회 일때 (k>=2) k회 나온 메뉴 저장
        if len(cnt) > 0 and max(cnt.values()) >= 2:
            max_val = max(cnt.values())
        
        for k, v in cnt.items():
            if v == max_val:
                answer.append(''.join(k))
    
    return sorted(answer)


# test case 
answer = 	["WX", "XY"]
my_answer = solution(["XYZ", "XWY", "WXA"],[2,3,4])
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

