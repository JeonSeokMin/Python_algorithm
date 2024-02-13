from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())

# 모든 노드의 대한 진입차수를 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for i in range(v+1)]

# 각 강의 시간을 0 으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)  # j 에서 i 로 이동가능

def topology_sort():
    result = copy.deepcopy(time)    # 알고리즘 수행 결과를 담을 리스트
    queue = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 때까지 반복
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    # 위상 정렬 수행 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()
