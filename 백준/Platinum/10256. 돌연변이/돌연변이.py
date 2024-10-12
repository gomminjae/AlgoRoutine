from collections import deque
import sys 
input = sys.stdin.readline

def tonum(c):
    if c == 'A':
        return 0
    elif c == 'G':
        return 1
    elif c == 'T':
        return 2
    else:
        return 3


class Trie:
    def __init__(self):
       
        self.ch = [None] * 4
        self.end = False  
        self.fail = None  

    
    def insert(self, s):
        node = self
        for char in s:
            now = tonum(char)
            if node.ch[now] is None:
                node.ch[now] = Trie()
            node = node.ch[now]
        node.end = True

  
    def init(self):
        q = deque([self])
        self.fail = self  
        while q:
            node = q.popleft()
            for i in range(4):
                child = node.ch[i]
                if child is None:
                    continue
                if node == self:
                    child.fail = self
                else:
                    fail_node = node.fail
                    while fail_node != self and fail_node.ch[i] is None:
                        fail_node = fail_node.fail
                    if fail_node.ch[i]:
                        child.fail = fail_node.ch[i]
                    else:
                        child.fail = self
                if child.fail.end:
                    child.end = True
                q.append(child)

    
    def query(self, s):
        global ans
        node = self
        for char in s:
            now = tonum(char)
            while node != self and node.ch[now] is None:
                node = node.fail
            if node.ch[now]:
                node = node.ch[now]
            if node.end:
                ans += 1


if __name__ == "__main__":
    T = int(input())  
    for _ in range(T):
        n, m = map(int, input().split())  
        a = input().strip()  
        b = input().strip() 
        
      
        root = Trie()
        ans = 0
        
       
        root.insert(b)
        
        
        for i in range(len(b)):
            for j in range(i + 1, len(b)):
                tmp = list(b)
                tmp[i:j + 1] = reversed(tmp[i:j + 1])
                root.insert("".join(tmp))
        
        
        root.init()
        
        
        root.query(a)
        
        
        print(ans)