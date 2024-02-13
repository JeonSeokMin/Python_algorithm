# disjoin_set.py 처럼 구현하면 답을 구할 수는 있지만, find 함수가 비효율적으로 동작한다.
# 예시) 1 <- 2 <- 3 <- 4 <- 5 이렇게 일렬로 나열된 형태에서 5번 노드의 루트 노드를 찾으려면
# 노드 5번 부터 부모노드를 거슬러 올라가야 한다. 이러한 문제를 해결하기 위해, Path Compression 을 사용한다.

# 요약 : Path Compression 은 find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신한다.

def find_parent(parent, x):

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])      
    
    return parent[x]        # 이렇게 하게 되면 find 함수를 호출한 뒤에 해당 노드의 루트 노드가 바로 부모 노드가 된다.