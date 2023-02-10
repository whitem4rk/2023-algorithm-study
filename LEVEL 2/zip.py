# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / 문자열 압축

# 마지막 값 처리를 못해서 실패한 문제 / 발상은 쉬운데 구현이 쉽지 않음
def solution(s):
    result = []
    s_len = len(s)
    
    # 예외처리
    if s_len==1:
        return 1
    
    # 구분짓는 문자열수는 절반까지만 해도 충분
    for i in range(1, len(s)//2+1):
        # 인덱스 0인 값부터 저장
        b = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, s_len+i, i):
            if tmp == s[j:j+i]:
                cnt+=1
            else:
                if cnt != 1:
                    b += str(cnt)+tmp
                else:
                    b += tmp
                tmp = s[j:j+i]
                cnt = 1
        
        result.append(len(b))
    return min(result)

# test case / answer = 7
print(solution("aabbaccc"))