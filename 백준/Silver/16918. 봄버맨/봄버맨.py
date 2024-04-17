import sys 
input = sys.stdin.readline
from collections import deque 

dx = [0,0,1,-1]
dy = [1,-1,0,0]

bomb = deque()

def setup_bomb():
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'


def pung():
    while bomb:
        x,y = bomb.popleft() 
        board[x][y] = '.'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                board[nx][ny] = '.'    
    for i in range(r):
        for j in range(c):
            if board[i][j] =='O':
                bomb.append((i,j))
    

        
    
r,c,n = map(int,input().split())
board = [] 

for _ in range(r):
    board.append(list(input().rstrip()))

for i in range(r):
    for j in range(c):
        if board[i][j] =='O':
            bomb.append((i,j))

start = 0 
for i in range(1,n):
    if i % 2 == 0:
        pung()
    else:
        setup_bomb()


for i in range(r):
    print(''.join(board[i]))

    
    