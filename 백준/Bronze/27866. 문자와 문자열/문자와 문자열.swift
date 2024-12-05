import Foundation

let s = readLine()!
let n = Int(readLine()!)!

let index = s.index(s.startIndex, offsetBy: n-1)

print(s[index])
