import sys
input = sys.stdin.readline
                          
class Node:
  def __init__(self, c):
    self.c = c
    self.childrens = {}
    self.count = 0
    self.is_end = False

class Trie:
  def __init__(self):
    self.root = Node('R')

  def insert(self, strr):
    cur = self.root

    for c in strr:     
     
      if not cur.childrens.get(c):   
        cur.childrens[c] = Node(c)  
      
      cur = cur.childrens[c]     
      cur.count += 1

    cur.is_end = True

  def dfs(self, node, type_count):
    if node.count == 1:
     
      return type_count

    res = 0
    if node.is_end:
     
      res += type_count     

    for next_node in node.childrens.values():     
    
      if node.count == next_node.count:
        next_type_count = type_count
      else:
        next_type_count = type_count + 1

      res += self.dfs(next_node, next_type_count)

    return res

if __name__ == '__main__':
  while True:
    try:
      N = int(input())  
    except:
      break

    trie = Trie()    
    for _ in range(N):               
      trie.insert(str(input().rstrip()))

    print('%0.2f' % (trie.dfs(trie.root, 0) / N))