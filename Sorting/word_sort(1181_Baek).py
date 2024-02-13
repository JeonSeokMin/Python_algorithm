N = int(input())

words = [str(input()) for _ in range(N)]

# 중복 제거
word = list(set(words))

# 알파벳 순으로 정렬
word.sort()

# 길이 순으로 정렬
word.sort(key=len)

for i in range(len(word)):
    print(word[i], end=' ')