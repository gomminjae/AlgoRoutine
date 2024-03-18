def solution(food):
    result = []
    
    food_length = []

    for i in range(1,len(food)):
        fl = food[i] // 2 
        food_length.append(fl)
    
    
    
    for i in range(food[0]):
        result.append(0)

    for i in range(len(food_length)-1,-1,-1):
        for j in range(food_length[i]):
            result.append(i+1)
            result.insert(0,i+1)

    return ''.join(map(str,result))
        
    
