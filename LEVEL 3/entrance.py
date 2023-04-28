# 코딩테스트 연습 / 이분탐색 / 입국심사
# 실패

def solution(n, times):
    answer = 0

    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for time in times:
            cnt += mid // time
            if n <= cnt:
                break

        if n <= cnt:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer
