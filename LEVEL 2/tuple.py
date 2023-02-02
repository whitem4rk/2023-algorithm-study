# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 튜플

# 다른사람 풀이
# import re
# from collections import Counter

# def solution(s):
#     s = Counter(re.findall('\d+', s))
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


def solution(s):
    answer = []
    # 입력값 파싱, 길이별로 정렬
    s_list = s[2:-2].split('},{')
    s_list.sort(key=len)
    
    # 차집합을 사용해서 하나씩 추가
    cur_set = set()
    for obj in s_list:
        obj_set = set(map(int,obj.split(',')))
        diff = list(obj_set - cur_set)
        cur_set = obj_set
        answer.append(diff[0])
        
    return answer

# test case / answer = 2
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))