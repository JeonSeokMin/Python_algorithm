A, B = map(int,input().split())

X = abs(A-B)

N = int(input())
a = 1001
fav_list = []

for i in range(N):
    fav_list.append(abs(int(input())-B) + 1)

for i in range(N):
    a = min(X, fav_list[i], a)

print(a)