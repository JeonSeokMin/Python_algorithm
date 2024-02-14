N, M = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    
    total = 0
    mid = (start + end) // 2

    for tteok in array:

        if tteok > mid:
            total += (tteok - mid)

    if total < M:
        end = mid - 1

    elif total > M:
        start = mid + 1

    else:
        break

print(mid)