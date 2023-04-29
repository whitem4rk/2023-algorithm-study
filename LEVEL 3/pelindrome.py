# 코딩테스트 연습 / 연습문제 / 가장 긴 팰린드롬
# 실패 

def solution(s):
    answer = 1                 
    for i in range(len(s)):           
        for j in range(i,len(s)+1):   
            if s[i:j] == s[i:j][::-1]: 
                answer = max(answer, len(s[i:j])) 
    return answer