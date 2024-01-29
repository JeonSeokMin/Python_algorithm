n = int(input())

Lv_list = list(map(int, input().split()))
    
Lv_list.sort(reverse=True)

gold = 0

for i in range(1, len(Lv_list)):
    gold += Lv_list[0] + Lv_list[i]
    
print(gold)