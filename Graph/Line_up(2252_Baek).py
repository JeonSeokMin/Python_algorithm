from collections import deque

import sys

N, M = map(int, input().split())

Edges = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    Edges[a].append(b)

    indegree[b] += 1

def topology_sort():

    queue = deque()

    result = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()

        result.append(now)

        for i in Edges[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()
