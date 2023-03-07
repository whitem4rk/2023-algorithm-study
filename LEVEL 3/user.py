# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 불량 사용자

from itertools import combinations, permutations
import re

def solution(user_id, banned_id):
    answer = 0
    # user_id 조합 생성
    combine = list(combinations(user_id, len(banned_id)))
    combine = [ list(comb) for comb in combine ]    
    # ban목록을 정규식으로 표현
    banned_id = [ '^'+ban.replace('*','.')+'$' for ban in banned_id ]

    for comb in combine:
        # user id 조합에서 ban에 해당하는것을 하나씩 지우면서 len==0 이면 성공
        # 단, 지워지는 순서도 고려해야하므로 순열로 userid를 만들고 확인
        perm = list(permutations(comb, len(comb)))
        perm = [ list(p) for p in perm]
        for per in perm:
            for ban in banned_id:
                for p in per:
                    if re.match(ban, p) != None:
                        per.remove(p)
                        break
            
            if len(per) == 0:
                answer += 1 
                break
            
    return answer

# test case 
answer = 3
my_answer = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

