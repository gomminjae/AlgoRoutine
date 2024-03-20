from functools import cmp_to_key

def compare(x,y):
    if str(y)+str(x)>=str(x)+str(y):return 1
    else:return -1

def solution(numbers):
    numbers=sorted(numbers, key=cmp_to_key(compare))
    return str(int("".join(map(str,numbers))))