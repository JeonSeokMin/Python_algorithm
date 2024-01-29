def solution(k, m, score):
    
    score.sort()
    
    result_list = []
    price_list = []
    
    for i in range(len(score) // m):
        for j in range(m):
            result_list.append(score.pop())
            
        price_list.append(min(result_list)*m)
        result_list = []
        
    answer = sum(price_list)
    
    return answer