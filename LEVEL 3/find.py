# 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT / 길 찾기 게임

# 재귀 제한을 늘려야 한다고 한다...
import sys
sys.setrecursionlimit(10**6)

answer1 = []
answer2 = []
class Node:
    def __init__(self, x, y, data) -> None:
        self.x = x
        self.y = y
        self.data = data
        self.right = None
        self.left = None

    def insert(self, x, y, data):
        if x < self.x:
            if self.left is None:
                self.left = Node(x,y,data)
            else:
                self.left.insert(x, y, data)
        
        else:
            if self.right is None:
                self.right = Node(x,y,data)
            else:
                self.right.insert(x,y,data)
    
    def preorder(self, root):
        global answer1
        if root:
            answer1.append(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self, root):
        global answer2
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            answer2.append(root.data)
        

def solution(nodeinfo):
    answer = []
    nodelist = []
    for idx, node in enumerate(nodeinfo):
        nodelist.append((node[0],node[1],idx+1))
    nodelist.sort(key=lambda x: (-x[1],x[0]))
    print(nodelist)
    
    root = Node(nodelist[0][0], nodelist[0][1], nodelist[0][2])
    for i in range(1, len(nodelist)):
        x = nodelist[i][0]
        y = nodelist[i][1]
        data = nodelist[i][2]
        root.insert(x,y,data)
    
    root.preorder(root)
    root.postorder(root)
    answer.append(answer1)
    answer.append(answer2)
    return answer



answer = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
my = solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
print(my)
print('correct') if answer == my else print('wrong')