# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 순위 검색

# 처음에 문자별로 info를 정렬해서 값을 뽑아낼 생각이었으나 문자열 이진탐색이 불가능해서 실패
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    table = {}
    # 문장을 단어 배열로 변환
    info_list = [x.split() for x in info]
    query_list = [ x.replace('-', '') for x in query]
    query_list = [x.replace(' and', '').split() for x in query_list]
    
    for inform in info_list:
        for i in range(5):
            # ('-' 를 고려) 조합으로 값 dict에 저장
            for c in combinations(inform[:-1], i):
                key = ''.join(c)
                if key in table:
                    table[key].append(int(inform[-1]))
                else:
                    table[key] = [int(inform[-1])]
    
    # dict에 있는 모든 점수 정렬
    for key in table:
        table[key].sort()
    
    # query가 info에 있는지 확인하고 있다면 x점 이상인 개수 계산
    for q in query_list:
        key = ''.join(q[:-1])
        if key in table:
            answer.append(len(table[key]) - bisect_left(table[key], int(q[-1])))
        else:
            answer.append(0)
    
    return answer



# test case / answer = [1,1,1,1,2,4]
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
                ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


# 이진탐색, upper bound 이진탐색 차이 (from chatGPT)
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
    
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
    
#     return -1
# ------------------------------------------------------------------
# def upper_bound(arr, target):
#     low = 0
#     high = len(arr)
    
#     while low < high:
#         mid = (low + high) // 2
#         if arr[mid] <= target:
#             low = mid + 1
#         else:
#             high = mid
    
#     return low