from re import L
import sys 
input = sys.stdin.readline


vowels = ['a','e','i','o','u']

def check(li):
    v_count = 0
    c_count = 0 
    
    for ch in li:
        if ch in vowels:
            v_count += 1 
        else:
            c_count += 1 

    if c_count >= 2 and v_count >= 1:
        return True 
    else:
        False 

def backtracking(li):
    
    if len(li) == l:
        if check(li):
            print("".join(li))
            return

    for i in range(len(li),c):
        if li[-1] < words[i]:
            li.append(words[i])
            backtracking(li)
            li.pop() 
        
        

l,c = map(int, input().split())
words = list(input().split())
words.sort() 


for i in range(c-l+1):
    li = [words[i]]
    backtracking(li)