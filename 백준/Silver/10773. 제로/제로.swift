import Foundation

struct Stack<T>: Sequence {
    private var elements: [T] = []


    mutating func push(_ element: T) {
        elements.append(element)
    }


    mutating func pop() -> T? {
        return elements.popLast()
    }


    func top() -> T? {
        return elements.last
    }


    var size: Int {
        return elements.count
    }


    var isEmpty: Bool {
        return elements.isEmpty
    }

   
    func makeIterator() -> IndexingIterator<[T]> {
        return elements.makeIterator()
    }
}

let n = Int(readLine()!)!

var stack = Stack<Int>()

for _ in 0..<n {
    let n = Int(readLine()!)!
    
    if n == 0 {
        stack.pop()
    } else {
        stack.push(n)
    }
}
var result = 0
for i in stack {
    result += i
}

print(result)
