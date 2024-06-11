import sys
input = sys.stdin.readline

def is_two_rectangle_meet(rect1, rect2):
    if (rect1[1][0] < rect2[0][0] or rect2[1][0] < rect1[0][0] or
        rect1[0][1] > rect2[1][1] or rect2[0][1] > rect1[1][1]):  # 아예 만나지 않을 때
        return False
    elif ((rect1[0][0] < rect2[0][0] < rect2[1][0] < rect1[1][0] and
          rect1[0][1] < rect2[0][1] < rect2[1][1] < rect1[1][1]) or
          (rect2[0][0] < rect1[0][0] < rect1[1][0] < rect2[1][0] and
          rect2[0][1] < rect1[0][1] < rect1[1][1] < rect2[1][1])): # 면적이 겹치지만 안에 쏙 들어가있을 때
        return False
    else:
        return True
def is_contain_origin(rect):
    if (0 not in rect[0]) and (0 not in rect[1]):
        return False
    elif rect[0][0]*rect[1][0] > 0 or rect[0][1]*rect[1][1] > 0:
        return False
    else:
        return True
def find(node):
    if reps[node] != node:
        reps[node] = find(reps[node])
    return reps[node]
def union(node1, node2):
    rep1 = find(node1)
    rep2 = find(node2)
    reps[rep2] = rep1

N = int(input())
reps = list(range(N))
rects = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    rects.append(((x1, y1), (x2, y2)))

for i in range(N-1):
    for j in range(i+1, N):
        if is_two_rectangle_meet(rects[i], rects[j]):
            union(i, j)

for i in range(N):
    find(i)

total = len(set(reps))
for i in range(N):
    if is_contain_origin(rects[i]):
        total -= 1
        break

print(total)