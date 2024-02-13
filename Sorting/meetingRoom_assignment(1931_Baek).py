import sys

N = int(input())
time = []

for _ in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort()     # 처음 정렬 시 시작 시간의 오름차순으로 먼저 정렬을 해준 뒤 -> 끝나는 시간이 같을 경우 문제 발생.

time.sort(key= lambda x : x[1])     # 끝나는 시간 기준으로 다시 정렬

result = 0

meeting = time[0]   
result += 1

for i in range(1, len(time)):
    if time[i][0] >= meeting[1]:
        meeting = time[i]
        result += 1

print(result)