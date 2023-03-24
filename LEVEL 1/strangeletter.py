# 코딩테스트 연습 / 연습문제 / 이상한 문자 만들기
# 실패 - 문제 이해 확실히

def solution(s):
    answer = ''   
    real_cnt = 0
    
    for i in range(len(s)):
        if not s[i].isalpha():
            real_cnt = 0
            answer += s[i]
        else:
            if real_cnt % 2 ==0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            real_cnt += 1
    return answer