import sys
from math import inf

input = sys.stdin.readline

def cost(x):
    total_cost = 0
    for i in range(N):
        total_cost += abs(X[i] - x * i)
    return total_cost


N = int(input())
X = list(map(int, input().split()))

low, high = 1, 1000000000

while high - low >= 3:
    mid1 = (2 * low + high) // 3
    mid2 = (low + 2 * high) // 3
    
    
    if cost(mid1) < cost(mid2):
        high = mid2
    else:
        low = mid1

min_cost = inf
for x in range(low, high + 1):
    min_cost = min(min_cost, cost(x))

print(min_cost)