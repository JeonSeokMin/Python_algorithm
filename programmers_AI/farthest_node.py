from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    
    for i in range(len(edge)):
        a = edge[i][0]
        b = edge[i][1]
        
        graph[a] += [b]
        graph[b] += [a]
        
    visited = [0] * (n + 1)
    
    queue = deque([1])
    
    visited[1] = 1
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)
                
    max_value = max(visited)
    answer = visited.count(max_value)
    
    return answer

# -> 원래 양방향 연결을 표현할 때 반목문의 범위를 range(n + 1) 로 표현함. 이는 잘못된 것. 범위를 range(len(edge)) 로 해줘야 한다,
    
#---------------------------------------------------------------------#
# 정답 코드 #

# from collections import deque 
# def solution(n, edge):
#     graph = [[] for _ in range(n + 1)]
#     visited = [0] * (n + 1)    
    
#     for eg in edge:
#         a, b = eg[0], eg[1]
#         graph[a].append(b)
#         graph[b].append(a)
    
#     q = deque() 
#     q.append(1)
#     visited[1] = 1 
#     while q:
#         x = q.popleft() 
#         for i in graph[x]:
#             if not visited[i]:
#                 visited[i] = visited[x] + 1 
#                 q.append(i)
    
#     max_value = max(visited)
#     answer = visited.count(max_value)
    
#     return answer
            
    