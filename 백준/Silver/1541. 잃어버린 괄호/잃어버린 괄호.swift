import Foundation


let input = readLine()!

let groups = input.split(separator: "-").map { String($0) }

var result = groups[0].split(separator: "+").map { Int($0)! }.reduce(0, +)

for i in 1..<groups.count {
    let groupSum = groups[i].split(separator: "+").map { Int($0)! }.reduce(0, +)
    result -= groupSum
}

print(result)