from collections import deque
import sys 
input = sys.stdin.readline

def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

sx = sy = ex = ey = -1
dist = [[-1] * n for _ in range(n)]
dist2 = [[-1] * n for _ in range(n)]
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 'M':
            sx, sy = i, j
        if board[i][j] == 'D':
            ex, ey = i, j
        if board[i][j] == 'H':
            dist[i][j] = 0
            Q.append((i, j))

while Q:
    x, y = Q.popleft()
    for k in range(4):
        nx = x + int("1012"[k]) - 1
        ny = y + int("2101"[k]) - 1
        if OOB(nx, ny) or (board[nx][ny] != 'G' and board[nx][ny] != 'M'):
            continue
        if dist[nx][ny] != -1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        Q.append((nx, ny))

def Check(mid):
    if dist[sx][sy] <= mid:
        return False
    dist2 = [[-1] * n for _ in range(n)]
    dist2[sx][sy] = mid
    Q.append((sx, sy))

    cnt = 1
    while Q:
        for _ in range(m):
            for _ in range(len(Q)):
                x, y = Q.popleft()
                for k in range(4):
                    nx = x + int("1012"[k]) - 1
                    ny = y + int("2101"[k]) - 1
                    if OOB(nx, ny) or dist2[nx][ny] != -1:
                        continue
                    if board[nx][ny] == 'T':
                        continue
                    if dist[nx][ny] != -1 and dist[nx][ny] < mid + cnt:
                        continue
                    dist2[nx][ny] = mid + cnt
                    Q.append((nx, ny))
        
        for _ in range(len(Q)):
            x, y = Q.popleft()
            if dist[x][y] <= dist2[x][y]:
                continue
            Q.append((x, y))

        cnt += 1

    return dist2[ex][ey] != -1

lo, hi = -1, 10**6
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if Check(mid):
        lo = mid
    else:
        hi = mid

print(lo)