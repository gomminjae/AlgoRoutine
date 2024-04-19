import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    global count
    visited[v] = 1
    for i in adjList[v]:
        if not visited[ord(i)-65]:
            count += 1
            dfs(ord(i)-65)

n, m = map(int, input().split())
adjList = [[] for i in range(n)]
visited = [0 for i in range(n)]
root = [1 for i in range(n)]
for j in range(m):
    a, b = input().split()
    adjList[ord(a)-65].append(b)
    root[ord(b)-65] = 0
    
check = list(input().split())
check = check[1:]
for i in check:
    visited[ord(i)-65] = 1

count = 0
for i in range(n):
    if root[i] == 1 and not visited[i]:
        dfs(i)
print(count)