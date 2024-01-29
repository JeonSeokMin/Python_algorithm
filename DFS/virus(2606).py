import sys

computer = int(input())     # 컴퓨터 개수 입력 받기

link = int(input())         # 연결되어 있는 컴퓨터 입력받기

graph = [[] for _ in range(computer+1)]     # 연결 정보를 리스트로 만들기 위해 2차원 리스트 생성

# computer + 1 만큼 생성하는 이유는 컴퓨터에 맞는 인덱스를 쓰기 위함.

visited = [0]*(computer + 1)        # 방문 리스트 생성.

for i in range(link):
    a, b = map(int, sys.stdin.readline().split())
    
    graph[a] += [b]     # 양방향 연결을 만들어서 인접 리스트를 생성한다.
    graph[b] += [a]
    
def dfs(v):
    visited[v] = 1      # 현재 노드를 방문 처리
    
    for i in graph[v]:      # 현재 노드와 연결되어 있는 노드 중에 
        if visited[i] == 0:     # 방문하지 않은 노드가 있다면
            dfs(i)          # 재귀 호출
            
dfs(1)      # 1번 노드에서 시작

print(sum(visited) - 1)         # -1 하는 이유는 자기 자신 노드 빼는 것.

    
