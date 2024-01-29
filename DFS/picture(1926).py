import sys
sys.setrecursionlimit(10 ** 6)      # 재귀 제한

cnt = []        # 그림의 개수

res = []        # 그림의 크기

n, m = map(int, input().split())

picture = []

for i in range(n):
    picture.append(list(map(int, sys.stdin.readline().split())))
    

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if picture[x][y] == 1:
        cnt.append(1)
        picture[x][y] = 0
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        
        return True
    
    return False


for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            dfs(i, j)
            res.append(len(cnt))
            cnt = []

print(len(res))

if len(res):
    print(max(res))
else:
    print(0)
