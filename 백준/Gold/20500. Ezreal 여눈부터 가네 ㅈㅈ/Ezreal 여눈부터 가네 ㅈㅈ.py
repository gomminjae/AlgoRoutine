import sys 
input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = (dp[i-1] * 2 + 1) % 1000000007
    else:
        dp[i] = (dp[i-1] * 2 - 1) % 1000000007
print(dp[n])