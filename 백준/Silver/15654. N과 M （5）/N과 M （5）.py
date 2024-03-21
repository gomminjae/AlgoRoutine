import sys 
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort() 
result = [] 
def dfs():

    if len(result) == m:
        print(' '.join(map(str,result)))
        return 


    for num in arr:
        if num not in result:
            result.append(num)
            dfs()
            result.pop()
dfs()