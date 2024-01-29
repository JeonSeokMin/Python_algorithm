N = int(input())
num_list = list(map(int, str(N)))
num_list.sort(reverse=True)

if(num_list[-1]) != 0:
    print("-1")
else:
    str_list = []
    for i in range(len(num_list)):
        str_list.append(str(num_list[i]))
    
    number="".join(str_list[0:-1])
    
    if(int(number) % 3) != 0:
        print("-1")
    else:
        number2="".join(str_list)
        print(number2)
    
     
