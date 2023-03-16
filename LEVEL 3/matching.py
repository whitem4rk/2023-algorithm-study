# 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT / 매칭 점수

from collections import defaultdict
import re

def solution(word:str, pages:list) -> int:
    
    # 모두 소문자 전환
    word = word.lower()
    for i in range(len(pages)):
        pages[i] = pages[i].lower()
    
    table = defaultdict(list)
    dictset = set()
    for idx, page in enumerate(pages):
        # 사이트 key에 넣고 초기화
        cur_url = re.search(r'<meta.+content="https:\/\/(.+)"\/>', page).groups()[0]
        if cur_url not in dictset:
            table[cur_url] = [0, 0, idx]
            dictset.add(cur_url)
        elif len(table[cur_url]) == 2:
            table[cur_url] = table[cur_url] + [idx]
        
        # 기본점수
        word_cnt = 0
        for w in re.findall(r'[a-z]+', page):
            if w == word:
                word_cnt += 1
        table[cur_url][0] = word_cnt
        
        # 점수 분배
        out_url = re.findall(r'<a href="https:\/\/([\S]+)">', page)
        out_cnt = len(out_url)
        
        for url in out_url:
            if url not in dictset:
                table[url] = [0, 0]
                dictset.add(url)
            table[url][1] += word_cnt / out_cnt
    
    answer = []
    for value in table.values():
        if len(value) == 3:
            answer.append(value)
            print(answer)
    answer.sort(key=lambda x: (-(x[0]+x[1]), x[2]))
    
    return answer[0][2]
        

answer = 1
my = solution('muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
print(my)
print('correct') if answer == my else print('wrong')