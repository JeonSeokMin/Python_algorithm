N = int(input())
coordinates = list(map(int, input().split()))

value = list(set(coordinates))
value.sort()

order = {}

for i in range(len(value)):
    order[value[i]] = i

for coordinate in coordinates:
    print(order[coordinate], end=' ')