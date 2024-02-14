# 가게의 부품 개수 입력받기
N = int(input())

# 계수를 받을 리스트 초기화
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록 
for i in input().split():
    array[int(i)] = 1

# 손님이 요청한 부품 수 입력받기
M = int(input())

# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
request = list(map(int, input().split()))

# 손님이 요청한 부품 번호 하나씩 확인
for item in request:
    # 해당 부품 있는지 확인
    if array[i] == 1:
        print("Yes", end=' ')

    else:
        print("No", end=' ')