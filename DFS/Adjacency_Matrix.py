# Python에서 그래프 표현(1) -> 인접 행렬

INF = 999999999     # 무한 비용 설정

graph = [[0, 7, 5],
         [7, 0 , INF],
         [5, INF, 0]]

print(graph)