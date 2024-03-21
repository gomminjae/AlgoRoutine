import sys
import heapq

N, M = map(int, input().split())
elec = list(map(int, input().split()))
elec.sort(reverse=True)
heap = []

for c in elec:
    if len(heap) < M:
        heapq.heappush(heap, c)
        #print(heap)
    else:
        time  = heapq.heappop(heap)
        #print(time)
        heapq.heappush(heap, time + c)

print(max(heap))