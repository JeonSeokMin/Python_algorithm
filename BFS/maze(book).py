from collections import deque
import time

start_time = time.time()    # 측정 시작

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input())))
    

# 상, 하, 좌, 우 처리
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
    
def bfs(x, y):
    
    # 방문 처리 위해 큐 자료 구조 만들어주기
    queue = deque()
    
    # 현재 노드 방문 처리
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 상, 하, 좌, 우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:      # N, M 자리 바뀌어야하는 거 아닌가..?
                continue
            
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                
                # 방문 처리
                queue.append((nx, ny))
                
    return graph[N-1][M-1]

print(bfs(0,0))

end_time = time.time()  # 측정 종료
print("time : ", end_time - start_time)
