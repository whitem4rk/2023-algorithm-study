# 코딩테스트 연습 / 2023 KAKAO BLIND RECRUITMENT / 개인정보 수집 유효기간
# 실패 - 0월은 없다는것을 빠뜨림



def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = map(int, today.split('.'))
    terms_dict = {}
    for t in terms:
        k, v = t.split()
        v = int(v) * 28
        terms_dict[k] = v
    
    for idx, priv in enumerate(privacies):
        date, term = priv.split()
        cur_y, cur_m, cur_d = map(int, date.split('.'))
        plus_d = terms_dict[term]
        plus_m, remain_d = divmod(cur_d+plus_d, 28)
        plus_y, remain_m = divmod(cur_m+plus_m, 12)
        if remain_m == 0:
            remain_m = 12
            plus_y -= 1
        remain_y = cur_y + plus_y
        remain_m = 12 if remain_m == 0 else remain_m
        print(remain_y, remain_m, remain_d)
        if t_y > remain_y:
            answer.append(idx+1)
        elif t_y == remain_y and t_m > remain_m:
            answer.append(idx+1)
        elif t_y == remain_y and t_m == remain_m and t_d >= remain_d:
            answer.append(idx+1)
    
    return answer