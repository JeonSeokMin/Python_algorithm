# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출.

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]
    
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

# 노드의 개수와 간선 개수 입력 받기
v, e = map(int, input().split())

# 부모 테이블 생성
parent = [0] * (v+1)

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보 입력받기
for i in range(e):
    a, b, cost = map(int, input().split())

    edges.append((cost, a, b))  # 비용순(오름차순)으로 정렬하기 위해 비용값을 첫번째 원소로 append

# 간선 리스트 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않았다면
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result) 

