from collections import deque

# 노드의 개수 및 간선의 개수를 받음
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())

    # 정점 a 에서 b 로 이동 가능
    graph[a].append(b)  

    # b 의 진입 차수를 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():

    # 알고리즘 수행 결과를 담을 리스트
    result = []

    queue = deque()

    # 처음 시작할 때는 진입 차수가 0 인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        # 큐에서 원소 꺼내기
        now = queue.popleft()

        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1

            # 새롭게 진입차수가 0 이 되는 노드들을 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

        # 위상 정렬을 수행한 결과 출력
        for i in result:
            print(i, end=' ')

topology_sort()




