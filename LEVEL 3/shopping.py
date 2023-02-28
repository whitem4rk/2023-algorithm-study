# 코딩테스트 연습 / 2020 카카오 인턴십 / 보석 쇼핑

def solution(gems):
    # 보석 종류 개수
    kind = len(set(gems))
    # 보석 개수 저장
    jewel_dict = {}
    # 보석 종류 개수와 저장된 종류개수가 같을때 그 구간을 기록
    gap_list = []
    start = 0
    
    for end, gem in enumerate(gems):
        if gem in jewel_dict:
            jewel_dict[gem] += 1
        else:
            jewel_dict[gem] = 1
            
        if kind == len(jewel_dict):
            for i in range(start, end):
                if jewel_dict[gems[i]] == 1:
                    start = i
                    break
                else:
                    jewel_dict[gems[i]] -= 1
            gap_list.append([start+1,end+1]) 
    gap_list.sort(key=lambda x: (x[1]-x[0]))
    return gap_list[0]

# test case 
answer = [3, 7]
my_answer = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

