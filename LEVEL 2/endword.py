# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 영어 끝말잇기
# 성공

def solution(n, words):
    wordset = set()
    
    before = words[0][0]
    for idx, word in enumerate(words):
        if word in wordset or before != word[0]:
            turn, num = divmod(idx, n)
            return [num+1, turn+1]
        
        before = word[-1]
        wordset.add(word)
    
    return [0, 0]