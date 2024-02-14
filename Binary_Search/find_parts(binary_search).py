def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

N = int(input())
items = list(map(int, input().split()))
M = int(input())
request = list(map(int, input().split()))

items.sort()

for item in request:
    result = binary_search(items, item, 0, N - 1)

    if result == None:
        print("No", end=' ')
    else:
        print("Yes", end=' ')