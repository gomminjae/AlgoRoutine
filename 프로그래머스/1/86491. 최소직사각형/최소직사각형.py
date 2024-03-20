
def solution(sizes):
    answer = 0
    width = 0 
    height = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp 

    print(sizes)
            
    for i in range(len(sizes)):
        if width < sizes[i][0]:
            width = sizes[i][0]
        if height < sizes[i][1]:
            height = sizes[i][1]
            
    answer = width * height 
    return answer 