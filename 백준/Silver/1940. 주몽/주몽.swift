import Foundation

let n = Int(readLine()!)!
let m = Int(readLine()!)!

var ingredients = readLine()!.split(separator: " ").map { Int($0)! }
ingredients.sort()

var left = 0
var right = ingredients.count - 1
var ans = 0

while left < right {
    if ingredients[left] + ingredients[right] < m {
      left += 1
    } else if ingredients[left] + ingredients[right] > m {
        right -= 1
    } else if ingredients[left] + ingredients[right] == m {
        ans += 1
        right -= 1
    }
}

print(ans)
