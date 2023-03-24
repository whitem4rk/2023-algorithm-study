# 코딩테스트 연습 / 2021 카카오 채용연계형 인턴십 / 숫자 문자열과 영단어
# 형변환

def solution(s):
    numdict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
              'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    for alpha, num in numdict.items():
        s = s.replace(alpha, num)
        
    return int(s)