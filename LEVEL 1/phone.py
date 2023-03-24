# 코딩테스트 연습 / 연습문제 / 핸드폰 번호 가리기
# 성공

def solution(phone_number):
    answer = '*' * (len(phone_number)-4)
    answer += phone_number[-4:]
    
    return answer