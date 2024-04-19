import sys 
input = sys.stdin.readline
from collections import deque 

#좌우상하
dx = [0,0,-1,1]
dy = [-1,1,0,0]

    

def ward(a,b):
    q = deque() 
    q.append((a,b))
    node = arr[a][b]
    visited[a][b] = 1 
    
    while q:
        x,y = q.popleft()
        isekai[x][y] = '.'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if arr[nx][ny] == node:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1 
                        isekai[nx][ny] = '.'
                        q.append((nx,ny))
        
    
r,c = map(int, input().split())
arr = [] 

for _ in range(r):
    arr.append(list(input().strip()))
hr,hc = map(int, input().split())
person = [hr-1,hc-1]
commands = list(input().strip())
isekai = [['#'] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]


for command in commands:
    if command == 'U':
        person[0] += dx[2]
        person[1] += dy[2]
    elif command == 'D':
        person[0] += dx[3]
        person[1] += dy[3]
    elif command == 'L':
        person[0] += dx[0]
        person[1] += dy[0]
    elif command == 'R':
        person[0] += dx[1]
        person[1] += dy[1]
    else:
        ward(person[0],person[1]) 

isekai[person[0]][person[1]] = '.'
for i in range(4):
    nx = person[0] + dx[i]
    ny = person[1] + dy[i]
    
    if 0<=nx<r and 0<=ny<c:
        isekai[nx][ny] = '.'

for i in range(r):
    print(''.join(isekai[i]))
    
