from collections import Counter
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

N, M = map(int, input().split())
map_list = [input().strip() for _ in range(N)]

def full_dfs(x, y, idx, visited):
    q = [(x, y)]
    visited[y][x] = idx
    while q:
        x, y = q.pop()
        for k in range(8):
            ax, ay = x + dx[k], y + dy[k]
            if -1 < ax < M and -1 < ay < N and map_list[ay][ax] == 'x' and visited[ay][ax] == -1:
                visited[ay][ax] = idx
                q.append((ax, ay))

def inside_dfs(x, y, idx, visited):
    is_outside = False
    contact_set = set()
    q = [(x, y)]
    while q:
        x, y = q.pop()
        for k in range(4):
            ax, ay = x + dx[k], y + dy[k]
            if -1 < ax < M and -1 < ay < N:
                if visited[ay][ax] == -1:
                    visited[ay][ax] = idx
                    q.append((ax, ay))
                elif visited[ay][ax] != idx:
                    contact_set.add(visited[ay][ax])
            else:
                is_outside = True
    return is_outside, contact_set

visited = [[-1] * M for _ in range(N)]
target_node = []
idx = 0
for i in range(N):
    for j in range(M):
        if map_list[i][j] == 'x' and visited[i][j] == -1:
            full_dfs(j, i, idx, visited)
            target_node.append((j, i))
            idx += 1

if not target_node:
    print(-1)
else:
    contact_dict = {}
    outside_list = []
    for idx, (x, y) in enumerate(target_node):
        local_visited = [_visited[:] for _visited in visited]
        is_outside, contact_set = inside_dfs(x, y, idx, local_visited)
        if is_outside:
            outside_list.append(idx)
        contact_dict[idx] = contact_set

    for i in range(idx + 1):
        for j in contact_dict[i]:
            contact_dict[j].add(i)

    inside_visited = [x in outside_list for x in range(idx + 1)]
    score_list = [0] * (idx + 1)

    def bfs(node):
        nxt_list = []
        for nxt in contact_dict[node]:
            if not inside_visited[nxt]:
                inside_visited[nxt] = True
                nxt_list.append(nxt)

        result = 0
        for nxt in nxt_list:
            result = max(result, bfs(nxt) + 1)

        score_list[node] = result
        return result

    for node in outside_list:
        bfs(node)

    maxval = max(score_list)
    counter = Counter(score_list)
    fscore_list = [0] * (maxval + 1)
    for key, val in counter.items():
        fscore_list[key] = val

    print(*fscore_list)