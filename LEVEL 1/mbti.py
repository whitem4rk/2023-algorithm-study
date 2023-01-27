# 코딩테스트 연습 / 2023 KAKAO TECH INTERNSHIP / 성격 유형 검사하기

def solution(survey, choices):
    # 아무런 입력이 없을때 RCJA로 시작
    answer = 'RCJA'
    
    table = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score_table = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    
    # mbti에 맞게 score 추가
    for mbti, score in zip(survey, choices):
        if score < 4:
            table[mbti[0]] += score_table[score]
        elif score > 4:
            table[mbti[1]] += score_table[score]
    
    table_list = list(table.items())
    
    # 2개씩 묶어서 비교하면서 최종 answer 도출
    for i in range(0,8,2):
        if table_list[i][1] < table_list[i+1][1]:
            answer = answer.replace(table_list[i][0], table_list[i+1][0])
            
    return answer

# test case / answer = "TCMA"
print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))