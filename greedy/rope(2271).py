K = int(input())

rope_weight = []

for i in range(K):
    rope_weight.append(int(input()))
    
rope_weight.sort()

weight = []

for i in range(1, K+1):
    weight.append(rope_weight[-i]*i)

weight.sort()
print(weight[-1])

