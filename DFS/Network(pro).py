# 프로그래머스 네트워크 수 찾는 문제.

def solution(n, computers):
    
    visited = [False] * n       # 방문 리스트를 만든다.
    
    def dfs(v):                 # dfs 함수. v는 현재 노드
        visited[v] = True       # 현재 노드를 방문 처리
        
        for i in range(n):      
            if not visited[i] and computers[v][i]:      # 현재 노드와 연결되어 있는 노드 중에 방문 되지 않은 노드 dfs 함수 호출하여 방문 처리
                dfs(i)
                
    answer = 0      # 네트워크 개수 변수
    
    for j in range(n):      # 컴퓨터 순회
        if not visited[j]:  # 방문하지 않은 노드
            dfs(j)          # 깊이 탐색
            answer += 1     # 깊이 탐색이 끝나면 네트워크 개수 올리기.
    
    return answer