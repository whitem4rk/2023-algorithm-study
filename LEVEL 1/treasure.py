# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []
    
    
    for a, b in zip(arr1, arr2):
        # OR 연산후 비는 부분을 0으로 채우고 치환 
        c = (a | b)
        c_str = bin(c)[2:].zfill(n)
        c_str = c_str.replace('1', '#')
        c_str = c_str.replace('0', ' ')

        answer.append(c_str)
    return answer


# test case / answer = ["#####","# # #", "### #", "# ##", "#####"]
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))