# 코딩테스트 연습 / 2023 KAKAO BLIND RECRUITMENT / 개인정보 수집 유효기간
# 다른풀이로는 한달이 28일로 고정되어있다는 점을 이용하여 일 수 비교로 풀 수 있다.

def solution(today, terms, privacies):
    answer = []
    # 오늘의 날짜
    t_y, t_m, t_d = map(int, today.split('.'))
    
    # { name : period }로 계약 저장
    terms_dict = {}
    for obj in terms:
        name, period = obj.split()
        terms_dict[name] = int(period)
    
    # privacies 반복문으로 비교 시작
    for i in range(len(privacies)):
        # privacy에 포함된 내용 파싱
        cur_date = privacies[i][:10]
        cur_terms = privacies[i][-1]
        cur_y, cur_m, cur_d = map(int,cur_date.split('.'))
        cur_period = terms_dict[cur_terms]
        
        # 월에만 덧셈 적용
        cur_m += cur_period
        
        # plus_y = 추가되어야 할 년도
        plus_y = ((cur_m-1) // 12) 
        cur_y += plus_y
        cur_m -= 12 * plus_y
        
        # 년-월-일 순으로 비교하면서 필터링을 통과하면 append
        if t_y < cur_y:
            continue
        elif t_y == cur_y:
            if t_m < cur_m:
                continue
            elif t_m == cur_m:
                if t_d < cur_d:
                    continue
        
        answer.append(i+1)
        
    return answer


# test case / answer = [1, 3]
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))