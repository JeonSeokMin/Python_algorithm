from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    answer = 0
    
    # 사각형 요소 중 최대 값 찾기
    
    def find_maxValue(rectangle):
        
        check = []
        
        for i in rectangle:
            check.append(max(i))
            
        return max(check)
    
    maxElement = find_maxValue(rectangle)
    
    # 최대값의 2배만큼 그래프 만들기
    
    graph = [[0]*(2*(maxElement + 1)) for _ in range((2*(maxElement + 1)))]
    
    # 사각형으로 지도 생성
    for i in rectangle:
        for j in range(i[0]*2, i[2]*2 + 1):
            for k in range(i[1]*2, i[3]*2 + 1):
                graph[j][k] = 1
                
    # 사각형 내부 비우기
    for i in rectangle:
        for j in range((i[0]*2)+1, (i[2]*2)):
            for k in range((i[1]*2)+1, (i[3]*2)):
                graph[j][k] = 0 
                
            
    queue = deque()
    
    queue.append((2*characterX, 2*characterY))
    
    visited = [[1]*(2*(maxElement + 1)) for _ in range((2*(maxElement + 1)))]
    
    visited[2*characterX][2*characterY] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < len(graph) and ny < len(graph[0]):  # 추가된 부분
                if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
            
    return answer
           
    # # 탐색
    # def bfs(x, y, dest_X, dest_Y):
    
    #     queue = deque()
        
    #     queue.append((2*x, 2*y))
        
    #     visited[2*x][2*y] = True
        
    #     dx = [-1, 1, 0, 0]
    #     dy = [0, 0, -1, 1]
        
    #     while queue:
    #         x, y = queue.popleft()
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
                
    #             if nx < 0 or nx >= (2*maxElement) or ny < 0 or ny >= (2*maxElement):
    #                 continue
                    
    #             if graph[nx][ny] == 0:
    #                 continue
                
    #             if graph[nx][ny] == 1 and visited[nx][ny] == False:
    #                 graph[nx][ny] = graph[x][y] + 1
    #                 queue.append((nx, ny))
    #                 visited[nx][ny] = True

                    
    #     return graph[2*dest_X - 1][2*dest_Y - 1]
            
        
    # answer = 0
    # return answer