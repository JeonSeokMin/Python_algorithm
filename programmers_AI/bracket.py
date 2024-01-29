from collections import deque

def solution(s):
    
    answer = True

    
    queue = deque(s)
    stack = []
    
    if len(queue) % 2 == 1:
        answer = False
    
    else:
        while queue:
            check = queue.popleft()
            
            if check == '(':
                stack.append(check)
                
            else:
                if stack:
                    stack.pop()
                
                else:
                    answer = False
                    
        if stack:
            answer = False
            
    return answer