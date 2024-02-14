N = int(input())

array = set(map(int, input().split()))

M = int(input())

request = list(map(int, input().split()))

for item in request:
    if item in array:
        print("Yes", end=' ')

    else:
        print("No", end=' ')