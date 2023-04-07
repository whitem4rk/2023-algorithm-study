# 코딩테스트 연습 / 해시 / 전화번호 목록
# 성공

def solution(phone_book):
    phone_book.sort()
    cur = phone_book[0]
    for i in range(1, len(phone_book)):
        if cur == phone_book[i][:len(cur)]:
            return False
        cur = phone_book[i]
    return True