import sys 
input = sys.stdin.readline


def play(target,n,expression):
    if target == n:
        if eval(expression.replace(" ","")) == 0:
            print(expression)
        return 

    relation = expression + " " + str(target + 1)
    play(target + 1, n, relation)
    
    plus = expression + "+" + str(target + 1)
    play(target + 1, n, plus)
    
    minus = expression + "-" + str(target + 1)
    play(target + 1, n, minus)


T = int(input())

for _ in range(T):
    n = int(input())
    play(1,n,"1")
    print()