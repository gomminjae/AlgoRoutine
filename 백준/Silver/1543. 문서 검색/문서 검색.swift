import Foundation

let s = readLine()!
let target = readLine()!

var cnt = 0
var index = 0

while index <= s.count - target.count {
    let start = s.index(s.startIndex, offsetBy: index)
    let end = s.index(start, offsetBy: target.count)
    let subString = s[start..<end]
    
    if subString == target {
        cnt += 1
        index += target.count
    } else {
        index += 1
    }
}



print(cnt)
