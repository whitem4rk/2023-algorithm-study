# 코딩테스트 연습 / 연습문제 / 행렬의 곱셈
# 실패 - 행렬 혼동

def solution(arr1, arr2):
    answer = [ [0] * len(arr2[0]) for _ in range(len(arr1)) ]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += arr1[i][k] * arr2[k][j]
            answer[i][j] = tmp
            
    return answer