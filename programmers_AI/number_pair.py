# def solution(X, Y):
    
#     X_list = [int(char) for char in X if char.isdigit()]
#     Y_list = [int(char) for char in Y if char.isdigit()]
    
#     X_list.sort(reverse=True)
#     Y_list.sort(reverse=True)
    
#     same_list = []
    
#     if len(X_list) > len(Y_list):
#         for i in Y_list.copy():
#             if i in X_list:
#                 same_list.append(i)
#                 X_list.remove(i)
#                 Y_list.remove(i)
            
#     elif len(Y_list) > len(X_list):
#         for i in X_list.copy():
#             if i in Y_list:
#                 same_list.append(i)
#                 X_list.remove(i)
#                 Y_list.remove(i)
            
#     elif len(Y_list) == len(X_list):
#         for i in X_list.copy():
#             if i in Y_list:
#                 same_list.append(i)
#                 X_list.remove(i)
#                 Y_list.remove(i)
                
#     if not same_list:
#         result = '-1'
#     elif all(element == 0 for element in same_list):
#         result = '0'
        
#     else:
#         result_list = [str(num) for num in same_list]
#         result = ''.join(result_list)
        
#     return result

# 위의 코드 테스트 케이스는 맞지만 시간 초과 문제 발생
# 해결 방안 -> collection의 counter 사용


def solution_1(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
    
def solution_2(X, Y):
    xList = list(X.count(str(x)) for x in range(10))
    yList = list(Y.count(str(y)) for y in range(10))
    answer = ""
    for i in range(9, -1, -1):
        answer += str(i) * min(xList[i], yList[i])

    if answer == "":
        return "-1"
    elif answer[0] == "0" and answer[len(answer) - 1] == "0":
        return "0"
    else:
        return answer