package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	board   [10][10]int
	empties []pair
)

type pair struct {
	x, y int
}


func printBoard() {
	for i := 1; i <= 9; i++ {
		for j := 1; j <= 9; j++ {
			fmt.Print(board[i][j])
		}
		fmt.Println()
	}
}


func isPossible(x, y, k int) bool {
	for i := 1; i <= 9; i++ {
		
		if board[x][i] == k && i != y {
			return false
		}
	
		if board[i][y] == k && i != x {
			return false
		}

		
		nx := (x-1)/3*3 + 1 + (i-1)/3
		ny := (y-1)/3*3 + 1 + (i-1)%3
		if board[nx][ny] == k && !(nx == x && ny == y) {
			return false
		}
	}
	return true
}


func backTracking(idx int) {

	if idx == len(empties) {
		printBoard()
		os.Exit(0)
	}

	x := empties[idx].x
	y := empties[idx].y
	for k := 1; k <= 9; k++ {
		
		if isPossible(x, y, k) {
			board[x][y] = k
			backTracking(idx + 1)
			
			board[x][y] = 0
		}
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for i := 1; i <= 9; i++ {
		scanner.Scan()
		line := scanner.Text()
		for j := 1; j <= 9; j++ {
			board[i][j] = int(line[j-1] - '0')
			if board[i][j] == 0 {
				empties = append(empties, pair{i, j})
			}
		}
	}

	backTracking(0)
}