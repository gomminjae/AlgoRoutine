from collections import deque 

def solution(begin, target, words):
    
    #없을때 
    if target not in words:
        return 0 
    
    q = deque()
    q.append((begin,0))
    result = []
    
    while q:
        w,d = q.popleft()
        
        if w == target:
            return d
            
        for word in words:
            cnt = 0 
            for i in range(len(word)):
                if w[i] == word[i]:
                    cnt += 1 
                    
            if cnt == len(word) - 1:
                q.append((word,d+1))       
        