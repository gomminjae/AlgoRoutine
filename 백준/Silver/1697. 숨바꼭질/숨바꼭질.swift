import Foundation


let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0]
let k = input[1]

var grid = Array(repeating: -1, count: 100001)

var q = [(n)]
grid[n] = 0

func bfs() -> Int {
    while !q.isEmpty {
        let position = q.removeFirst()
        
    
        if position == k {
            return grid[position]
        }
        
        for nx in [position - 1, position + 1, position * 2] {
            if nx >= 0 && nx <= 100000 && grid[nx] == -1 {
                grid[nx] = grid[position] + 1
                q.append(nx)
            }
        }
    }
    return -1
}

print(bfs())

