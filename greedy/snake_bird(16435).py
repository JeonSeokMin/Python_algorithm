N, L = map(int, input().split())

fruit_list = list(map(int, input().split()))

fruit_list.sort()

for i in range(len(fruit_list)):
    if(fruit_list[i] <= L):
        L += 1

print(L)
