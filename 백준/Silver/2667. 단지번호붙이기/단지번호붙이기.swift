import Foundation

let n = Int(readLine()!)!

var grid: [[Int]] = []



for i in 0..<n {
    grid.append(readLine()!.map { Int(String($0))! })
}

let dx = [-1,0,1,0]
let dy = [0,-1,0,1]

func bfs(x: Int, y: Int) -> Int {
    var q: [(Int, Int)] = [(x,y)]
    grid[x][y] = 0
    var count = 0
    
    while !q.isEmpty {
        let (cx,cy) = q.removeFirst()
        count += 1
        
        for i in 0..<4 {
            let nx = cx + dx[i]
            let ny = cy + dy[i]
            
            if nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] == 1 {
                grid[nx][ny] = 0
                q.append((nx, ny))
            }
        }
    }
    
    return count
}

var complexCounts: [Int] = []

for i in 0..<n {
    for j in 0..<n {
        if grid[i][j] == 1 {
            complexCounts.append(bfs(x: i, y: j))
        }
    }
}

complexCounts.sort()
print(complexCounts.count)
complexCounts.forEach { print($0) }


