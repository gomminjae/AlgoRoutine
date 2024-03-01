import sys 
input = sys.stdin.readline

def rotate(idx):
    global li 
    tmp = li[idx].pop()
    li[idx].insert(0,tmp)

def reverse_rotate(idx):
    global li 
    tmp = li[idx].pop(0)
    li[idx].append(tmp)

def clockwise(li,num):
    #2번이 오른쪽 6번이 왼쪽 
    flag1 = False
    flag2 = False
    flag3 = False 

    if li[0][2] != li[1][6]:
        flag1 = True 
    if li[1][2] != li[2][6]:
        flag2 = True 
    if li[2][2] != li[3][6]:
        flag3 = True 

    if num == 1:
        rotate(0)
        if flag1:
            reverse_rotate(1)
            if flag2:
                rotate(2)
                if flag3:
                    reverse_rotate(3)
        
    elif num == 2:
        rotate(1)
        if flag1:
            reverse_rotate(0)
        if flag2:
            reverse_rotate(2)
            if flag3:
                rotate(3)
            
    elif num == 3: 
        rotate(2)
        if flag2:
            reverse_rotate(1)
            if flag1:
                rotate(0)
        if flag3:
            reverse_rotate(3)
    
    elif num == 4:
        rotate(3)
        if flag3:
            reverse_rotate(2)
            if flag2:
                rotate(1)
                if flag1:
                    reverse_rotate(0)
        
    
    

def counterclockwise(li,num):
    flag1 = False
    flag2 = False
    flag3 = False 

    if li[0][2] != li[1][6]:
        flag1 = True 
    if li[1][2] != li[2][6]:
        flag2 = True 
    if li[2][2] != li[3][6]:
        flag3 = True 
    if num == 1:
        reverse_rotate(0)
        if flag1:
            rotate(1)
            if flag2:
                reverse_rotate(2)
                if flag3:
                    rotate(3)
    elif num == 2:
        reverse_rotate(1)
        if flag1:
            rotate(0)
        if flag2:
            rotate(2)
            if flag3:
                reverse_rotate(3)
    
    elif num == 3:
        reverse_rotate(2)
        if flag2:
            rotate(1)
            if flag1:
                reverse_rotate(0)
        if flag3:
            rotate(3)
    
    else:
        reverse_rotate(3)
        if flag3:
            rotate(2)
            if flag2:
                reverse_rotate(1)
                if flag1:
                    rotate(0)
li = [] 
for _ in range(4):
    li.append(list(input().rstrip()))
k = int(input())
for _ in range(k):
    number,direction = map(int,input().split())

    if direction == 1:
        clockwise(li,number)
    else:
        counterclockwise(li,number)

score = [1,2,4,8]
result = 0 
for i in range(4):
    if li[i][0] == '1':
        result += score[i]

print(result)