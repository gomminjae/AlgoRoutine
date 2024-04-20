
import sys 
input = sys.stdin.readline

s = list(map(str, input().strip())) 
stack = []

result = 0 

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    
    elif s[i-1] == ')':
        stack.pop()
        result += 1 
    
    else:
        stack.pop()
        result += len(stack)
        

print(result)
