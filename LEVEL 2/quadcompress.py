# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 쿼드압축 후 개수 세기
# 실패 - 아예 못품...

def solution(arr):
    answer = [0,0]
    
    def divide(x,y,N):
        standard = arr[x][y]
        for i in range(x, x+N):
            for j in range(y, y+N):
                if standard != arr[i][j]:
                    n = N // 2
                    divide(x,y,n)
                    divide(x+n,y,n)
                    divide(x,y+n,n)
                    divide(x+n,y+n,n)
                    return
        answer[standard] += 1
    
    divide(0,0,len(arr))
    return answer