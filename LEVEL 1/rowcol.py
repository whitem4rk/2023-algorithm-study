# 코딩테스트 연습 / 연습문제 / 행렬의 덧셈
# 실패 - 반복문 사용 미숙

def solution(arr1, arr2):
    answer = [[arr1[i][j]+arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
    return answer