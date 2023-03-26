# 코딩테스트 연습 / 해시 / 폰켓몬
# 성공

def solution(nums):
    select = len(nums) / 2
    nums = set(nums)
    return len(nums) if len(nums) <= select else select
