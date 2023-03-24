# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 비밀지도
# 실패 - zfill을 해줘야하는걸 생각하지 못함

def solution(n:int, arr1:list, arr2:list) -> list:
    answer = []
    for a,b in zip(arr1, arr2):
        tobin = str(bin(a|b))[2:]
        tobin = tobin.zfill(n)
        tobin = tobin.replace('1','#')
        tobin = tobin.replace('0',' ')
        answer.append(tobin)
    return answer
        