package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	inputs := strings.Fields(line)
	N, _ := strconv.Atoi(inputs[0])
	S, _ := strconv.Atoi(inputs[1])

	line, _ = reader.ReadString('\n')
	strSequence := strings.Fields(line)
	sequence := make([]int, N)
	for i := 0; i < N; i++ {
		sequence[i], _ = strconv.Atoi(strSequence[i])
	}

	prefix := make([]int, N+1)
	for i := 1; i <= N; i++ {
		prefix[i] = prefix[i-1] + sequence[i-1]
	}

	answer := 100001
	start, end := 0, 1
	for start < N {
		if prefix[end]-prefix[start] >= S {
			if answer > end-start {
				answer = end - start
			}
			start++
		} else {
			if end < N {
				end++
			} else {
				start++
			}
		}
	}

	if answer == 100001 {
		answer = 0
	}
	fmt.Println(answer)
}

