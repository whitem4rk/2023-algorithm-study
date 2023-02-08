# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] n진수 게임

num_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
                9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

# 10진수를 n진수로 반환
def ten_to_n(num:int, n:int) -> int:
    result = ''
    while num != 0:
        num, mod = divmod(num, n)
        result += (num_dict[mod])
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    numstring = '0'
    
    # 알아야하는 숫자는 m*t보다 작음이 분명하므로 n진수로 다 변환해서 문자열로 붙이기
    for i in range(m*t):
        numstring += str(ten_to_n(i,n))
    
    # p번째부터 +m을 했을때가 튜브가 말해야하는 문자
    for i in range(p-1, len(numstring), m):
        answer += numstring[i]
        # t번째까지 구했다면
        if len(answer) == t:
            break
    
    return answer

# test case / answer = "0111"
print(solution(2,4,2,1))