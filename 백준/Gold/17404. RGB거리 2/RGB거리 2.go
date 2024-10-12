package main

import (
	"bufio"
	"fmt"
	"os"
)

const INF = 987654321

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var N int
	fmt.Fscanf(reader, "%d\n", &N)


	arr := make([][3]int, N+1)
	dp := make([][3]int, N+1)

	for i := 1; i <= N; i++ {
		fmt.Fscanf(reader, "%d %d %d\n", &arr[i][0], &arr[i][1], &arr[i][2])
	}

	ans := INF

	
	for rgb := 0; rgb <= 2; rgb++ {
		
		for i := 0; i <= 2; i++ {
			if i == rgb {
				dp[1][i] = arr[1][i]
			} else {
				dp[1][i] = INF
			}
		}

		
		for i := 2; i <= N; i++ {
			dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
			dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
			dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
		}

		
		for i := 0; i <= 2; i++ {
			if i == rgb {
				continue
			}
			ans = min(ans, dp[N][i])
		}
	}

	fmt.Fprintf(writer, "%d\n", ans)
}
