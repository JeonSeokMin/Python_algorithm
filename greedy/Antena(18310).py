# N = int(input())

# house = list(map(int, input().split()))

# house.sort()

# sum = 0

# distance = {}

# outcome = []

# for i in house:
#     antena = i
#     for j in range(len(house)):
#         sum += abs(i - house[j])
#     distance[i] = sum
#     sum = 0
    
# key = [k for k, v in distance.items() if v == min(distance.values())]

# print(min(key))


#-------------------------------------------------------#

# 오름차순 후 중간값 찾으면 끝

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

print(arr[(N-1)//2])