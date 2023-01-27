# 코딩테스트 연습 / 2021 카카오 채용연계형 인턴십 / 숫자 문자열과 영단어

def solution(s):
    answer = 0
    # 문자열 : 숫자 대응 dict
    num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
                'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'ten':'10'}
    
    # 반복문에 쓰기 편하게 list 화
    num_list = list(num_dict.items())
    
    # 해당하는 문자열을 숫자로 치환
    for i in range(10):
        s = s.replace(num_list[i][0], num_list[i][1])
    
    answer = int(s)
    return answer

# test case / answer = 234567
print(solution('2three45sixseven'))