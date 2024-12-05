
import Foundation


struct Queue<T> {
    private var array: [T] = []
    private var head = 0

    var isEmpty: Bool {
        return head >= array.count
    }

    mutating func enqueue(_ element: T) {
        array.append(element)
    }

    mutating func dequeue() -> T? {
        guard !isEmpty else { return nil }
        let element = array[head]
        head += 1

        if head > 100 && head > array.count / 2 {
            array.removeFirst(head)
            head = 0
        }

        return element
    }
}


let input = readLine()!.split(separator: " ").map { Int($0)! }
let (m, n) = (input[0], input[1])

// 2차원 배열 입력받기
var grid: [[Int]] = []
for _ in 0..<n {
    grid.append(readLine()!.split(separator: " ").map { Int($0)! })
}

// 방향 벡터 (상, 하, 좌, 우)
let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

// BFS를 위한 큐
var queue = Queue<(Int, Int, Int)>()

// 초기 익은 토마토 위치를 큐에 넣기
for i in 0..<n {
    for j in 0..<m {
        if grid[i][j] == 1 {
            queue.enqueue((i, j, 0)) // 시작 좌표와 초기 날짜(0일)
        }
    }
}

var maxDays = 0 // 최대 날짜 저장

// BFS 실행
while let (x, y, days) = queue.dequeue() {
    maxDays = max(maxDays, days)

    // 상하좌우 탐색
    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]

        // 유효 범위 내에 있고 익지 않은 토마토라면
        if nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] == 0 {
            grid[nx][ny] = 1 // 익음 처리
            queue.enqueue((nx, ny, days + 1))
        }
    }
}

// 결과 확인
for row in grid {
    if row.contains(0) {
        print(-1) // 익지 않은 토마토가 남아 있으면 -1 출력
        exit(0)
    }
}

print(maxDays) // 모두 익었다면 최대 날짜 출력
