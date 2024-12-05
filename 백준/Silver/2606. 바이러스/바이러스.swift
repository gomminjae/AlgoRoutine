import Foundation

let n = Int(readLine()!)!
let m = Int(readLine()!)!

var graph = Array(repeating: [Int](), count: n+1)

for _ in 0..<m {
    let edge = readLine()!.split(separator: " ").map { Int($0)! }
    let (u,v) = (edge[0], edge[1])
    
    graph[u].append(v)
    graph[v].append(u)
}


func bfs(start: Int) -> Int {
    var visited = Array(repeating: false, count: n+1)
    var q: [Int] = [start]
    
    visited[start] = true
    
    var ans = 0
    
    while !q.isEmpty {
        let current = q.removeFirst()
        
        for i in graph[current] {
            if !visited[i] {
                visited[i] = true
                q.append(i)
                ans += 1
            }
        }
    }
    
    return ans
}


print(bfs(start: 1))