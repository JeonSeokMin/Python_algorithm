size = int(input())     # 지도 사이즈 입력받기

maps = []        # 지도 리스트 생성

for i in range(size):
    maps.append(list(map(int, input())))
    
home = 0        # 단지 내의 집의 수를 받을 변수

def dfs(x, y):
    if x <= -1 or x >= size or y <= -1 or y >= size:        # 지도를 벗어나는 경우 False 반환
        return False
    
    global home
    
    if maps[x][y] == 1:      # 집이 있는 경우
        home += 1           # 단지 내 집의 수에 추가하고
        maps[x][y] = 0       # 집의 위치를 다시 돌지 못하게 0으로
        
        dfs(x-1, y)         # 상하좌우 재귀호출
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        
        return True
    
    return False        # 집이 없는 경우 False 반환

num_list = []        # 단지 내의 집의 수를 받을 리스트 생성

for i in range(size):
    for j in range(size):       # 지도를 순회
        if dfs(i, j) == True:   
            num_list.append(home)    # 단지 내의 집의 수를 append
            home = 0            # 집의 수 초기화
            
num_list.sort()      # 오름차순 정렬

print(len(num_list))
for k in num_list:
    print(k)