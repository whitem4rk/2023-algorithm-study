# 코딩테스트 연습 / 2022 KAKAO TECH INTERNSHIP / 성격 유형 검사하기
# 성공

def solution(survey, choices):
    score_dict = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    
    for s, c in zip(survey, choices):
        c -= 4
        if s in score_dict:
            score_dict[s] += c
        else:
            score_dict[s[::-1]] -= c
            
    result = ''
    for obj, score in score_dict.items():
        if score > 0:
            result += obj[1]
        else:
            result += obj[0]
            
    return result
            