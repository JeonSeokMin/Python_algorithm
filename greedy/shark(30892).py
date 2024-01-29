from heapq import *

def max_weight(N, K, T, sharks):
    sharks.sort(reverse=True)  # 상어의 크기를 내림차순으로 정렬
    heap = []  # 힙 자료구조
    answer = T  # 초기 무게
    for _ in range(K):  # 먹을 수 있는 횟수만큼 반복
        while sharks and sharks[-1] < answer:  # 상어 리스트가 남아있고, 먹을 수 있는 상어가 있다면
            heappush(heap, -sharks.pop())  # 먹을 수 있는 상어를 힙에 추가
        if heap:  # 힙에 상어가 있다면
            answer -= heappop(heap)  # 가장 무게가 큰 상어를 먹음
        else:  # 먹을 수 있는 상어가 없다면
            break  # 반복 종료
    return answer  # 최종 무게 반환

N, K, T = map(int, input().split())
sharks = list(map(int, input().split()))
print(max_weight(N, K, T, sharks))  # 결과 출력