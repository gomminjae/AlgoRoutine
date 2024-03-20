from collections import deque

def make_graph(wires, n):
    cnt = 0
    graph = []

    for i in range(n + 1):
        node = []
        graph.append(node)

    for i in range(len(wires)):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

    return graph



def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    list = []

    while queue:
        v = queue.popleft()
        list.append(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return list

def solution(n, wires):
    answer = 100
    wires = sorted(wires, key = lambda x : (x[0], x[1]))

    # i번째 간선을 잘랐을 때
    for i in range(len(wires)):
        wire = wires[:i]+wires[i+1:]

        graph = make_graph(wire, n)

        # 탐색의 시작노드
        node = []
        node = set(node)
        for j in range(1, n + 1):
            visited = [False] * (n + 1)
            bfs(graph, j, visited)
            node.add(visited.count(True))

        if max(node) - min(node) < answer:
            answer = max(node) - min(node)

    return answer