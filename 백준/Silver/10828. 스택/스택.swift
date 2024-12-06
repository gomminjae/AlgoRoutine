import Foundation

struct Stack<T> {
    private var elements: [T] = []
    
    mutating func push(_ element: T) {
        elements.append(element)
    }
    
    mutating func pop() -> T? {
        return elements.popLast()
    }
    
    func peek() -> T? {
        return elements.last
    }
    
    var isEmpty: Bool {
        return elements.isEmpty
    }

    var count: Int {
        return elements.count
    }
}

let n = Int(readLine()!)!

var stack = Stack<Int>()

for _ in 0 ..< n {
    if let command = readLine() {
        let parts = command.split(separator: " ")
        let operation = parts[0]
        
        switch operation {
        case "push":
            if let value = parts.dropFirst().first, let number = Int(value) {
                stack.push(number)
            }
        case "pop":
            if let popped = stack.pop() {
                print(popped)
            } else {
                print(-1)
            }
        case "top":
            if let top = stack.peek() {
                print(top)
            } else {
                print(-1)
            }
        case "size":
            print(stack.count)
        case "empty":
            print(stack.isEmpty ? 1 : 0)
        default:
            break
        }
    }

}
