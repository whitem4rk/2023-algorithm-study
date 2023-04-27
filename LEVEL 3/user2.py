# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 불량 사용자
# 실패

from itertools import permutations

def solution(user_id, banned_id):
    permute = list(permutations(user_id, len(banned_id)))
    correct_list = []
    for per in permute:
        correct = True
        for i in range(len(banned_id)):
            if len(per[i]) != len(banned_id[i]):
                correct = False 
                break
            for c1, c2 in zip(per[i], banned_id[i]):
                if c2 == '*':
                    continue
                if c1 != c2:
                    correct = False
                    break
        if correct and set(per) not in correct_list:
            correct_list.append(set(per))
            print(f'success{per}')
    
    return len(correct_list)
