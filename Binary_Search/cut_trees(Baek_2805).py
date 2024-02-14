N, M = map(int, input().split())

array = list(map(int, input().split()))

start = 1

end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += (x - mid)

    if total < M:
        end = mid - 1

    else:
        start = mid + 1

print(end)