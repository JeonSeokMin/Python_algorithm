import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
list = []
for i in range(N):
    list.append(int(input()))

list.sort()

average = round(sum(list) / N)
print(average)

median = list[N // 2]
print(median)

cnt = Counter(list).most_common()    
if(len(list)>1 and (cnt[0][1] == cnt[1][1])):
    print(cnt[1][0])
else:
    print(cnt[0][0])
    
range = max(list) - min(list)
print(range)