N = int(input())
array = list(map(int, input().split()))
max_budget = int(input())

if sum(array) <= max_budget:
    print(max(array))
else:
    start = 0
    end = max(array)

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for x in array:
            if x > mid:
                total += mid
            else:
                total += x

        if total > max_budget:
            end = mid - 1
        else:
            start = mid + 1

    print(end)
