# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 뉴스 클러스터링
# 실패 - 예외처리

from collections import defaultdict

def solution(str1, str2):
    dict12 = defaultdict()
    
    for i in range(len(str1)-1):
        s = str1[i:i+2].lower()
        if s.isalpha():
            if s in dict12:
                dict12[s][0] += 1
            else:
                dict12[s] = [1,0]
    
    for i in range(len(str2)-1):
        s = str2[i:i+2].lower()
        if s.isalpha():
            if s in dict12:
                dict12[s][1] += 1
            else:
                dict12[s] = [0,1]
                
    if len(dict12) == 0:
        return 65536
    
    s, u = 0, 0
    for s1, s2 in dict12.values():
        s += max(s1,s2)
        u += min(s1,s2)
    return int(u/s * 65536)
    
        