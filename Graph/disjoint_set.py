def find_parent(parent, x):
    
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출

    if parent[x] != x:
        return find_parent(parent, parent[x])

    return x

def union_parent(parent, a, b):
    # 두 원소가 속한 집합 합치기

    a = find_parent(parent, a)  # a 의 부모노드
    b = find_parent(parent, b)  # b 의 부모노드

    if a < b:       
        parent[b] = a       # a 가 b 보다 작다면 a 가 b 의 부모노드
    else:
        parent[a] = b

v, e = map(int, input().split())    # 노드의 개수와 간선개수 입력받기
parent = [0] * (v + 1)      # 부모 테이블 초기화

for i in range(1, v+1):
    parent[i] = i           # 부모 테이블에서 부모를 자기 자신으로 초기화.

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)              # 유니온 연산 수행.

print('각 원소가 속한 집합: ', end='')       # 각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')