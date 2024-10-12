package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
    "strings"
)

var (
	N, M   int
	inDeg  [1002]int
	graph  [1002][]int
	result []int
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanln(reader, &N, &M)

	for i := 0; i < M; i++ {
		line, _ := reader.ReadString('\n')
		inputs := convertToInts(line)
		sNum := inputs[0]
		if sNum == 0 {
			continue
		}

		s1 := inputs[1]
		if sNum == 1 {
			continue
		}

		for j := 1; j < sNum; j++ {
			s2 := inputs[j+1]
			graph[s1] = append(graph[s1], s2)
			inDeg[s2]++
			s1 = s2
		}
	}

	queue := []int{}

	for i := 1; i <= N; i++ {
		if inDeg[i] == 0 {
			queue = append(queue, i)
		}
	}

	for len(queue) > 0 {
		s := queue[0]
		queue = queue[1:]
		result = append(result, s)

		for _, next := range graph[s] {
			inDeg[next]--
			if inDeg[next] == 0 {
				queue = append(queue, next)
			}
		}
	}

	if len(result) != N {
		fmt.Println(0)
	} else {
		for _, singer := range result {
			fmt.Println(singer)
		}
	}
}

func convertToInts(line string) []int {
	fields := bufio.NewScanner(strings.NewReader(line))
	fields.Split(bufio.ScanWords)
	var result []int
	for fields.Scan() {
		num, _ := strconv.Atoi(fields.Text())
		result = append(result, num)
	}
	return result
}
