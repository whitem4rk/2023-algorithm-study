# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 뉴스 클러스터링

from collections import Counter

def solution(str1, str2):
    answer = 0
    
    # 대문자 -> 소문자
    s1 = str1.lower()
    s2 = str2.lower()
    s1_list = []
    s2_list = []
    
    # 알파벳인지 확인하면서 2글자씩 넣기
    for i in range(len(s1)-1):
        if s1[i:i+2].isalpha():
            s1_list.append(s1[i:i+2])
    for i in range(len(s2)-1):
        if s2[i:i+2].isalpha():
            s2_list.append(s2[i:i+2])
    
    # 0/0 예외 처리
    if len(s1_list) == 0 and len(s2_list) == 0:
        rate = 1
    else:
        # Counter로 빈도수 구하고 합집합, 교집합 계산
        c1 = Counter(s1_list)
        c2 = Counter(s2_list)
        # 처음에 이렇게 짰는데 계속 런타임 에러가 떴다.
        # total()은 3.10부터 적용이라 버전문제가 있는듯 하다...
        # rate = ((c1&c2).total()) / ((c1|c2).total())
        a = list((c1&c2).elements())
        b = list((c1|c2).elements())
        rate = len(a) / len(b)
    
    answer =  int(rate * 65536)
    
    return answer

# test case / answer = 16384
print(solution('FRANCE','french'))