from collections import deque
import sys

N = int(input())

for _ in range(N):
    L = int(sys.stdin.readline())
    first_X, first_Y = map(int, sys.stdin.readline().split())
    last_X, last_Y = map(int, sys.stdin.readline().split())
    
    graph = [[0] * L for _ in range(L)]
    visited = [[False] * L for _ in range(L)]
    
    # 한 번에 갈 수 있는 

    dx = [-1, -1, 1, 1, -2, 2, 2, -2]
    dy = [2, -2, 2, -2, 1, 1, -1, -1]
    
    def bfs(x, y):
        
        if first_X == last_X and first_Y == last_Y:
            answer = 0
            return answer
        
        else:
            queue = deque()
            
            queue.append([x, y])
            
            while queue:
                x, y = queue.popleft()
                
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or ny < 0 or nx >= L or ny >= L:
                        continue
                    
                    if nx == last_X and ny == last_Y:
                        visited[nx][ny] == True
                        graph[nx][ny] = graph[x][y] + 1
                        return graph[nx][ny]
                
                    if visited[nx][ny] == False:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                        graph[nx][ny] = graph[x][y] + 1
                    
    
    answer = bfs(first_X, first_Y)
    print(answer)