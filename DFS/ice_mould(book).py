n, m = map(int, input().split())        # 얼음틀의 가로 세로 크기를 받는다.

graph = []      # 얼음틀의 형태를 저장할 리스트를 만들고

for i in range(n):
    graph.append(list(map(int, input())))       # 얼음틀 모양을 받는다.
    
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:      # 얼음틀 밖의 범위는 False를 반환한다.
        return False    
    
    if graph[x][y] == 0:        # 현재 노드를 방문하지 않았다면
        graph[x][y] = 1         # 방문 처리하고
        
        dfs(x-1, y)             # 상하좌우 위치 모두 재귀적으로 호출
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)