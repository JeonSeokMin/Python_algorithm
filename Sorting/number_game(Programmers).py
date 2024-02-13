def solution(A, B):

    A.sort(reverse= True)
    B.sort(reverse= True)

    answer = 0
    index = 0

    for a in A:
        if a < B[index]:
            answer += 1
            index += 1

    return answer