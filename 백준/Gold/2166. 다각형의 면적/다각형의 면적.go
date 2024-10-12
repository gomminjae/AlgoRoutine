package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)


	var n int
	fmt.Fscanf(reader, "%d\n", &n)

	
	coordList := make([][2]int, n+1)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d %d\n", &coordList[i][0], &coordList[i][1])
	}
	coordList[n] = coordList[0] 

	plus := 0
	minus := 0


	for i := 0; i < n; i++ {
		plus += coordList[i][0] * coordList[i+1][1]
		minus += coordList[i][1] * coordList[i+1][0]
	}

	
	area := math.Abs(0.5 * float64(plus-minus))

	
	fmt.Printf("%.1f\n", area)
}
