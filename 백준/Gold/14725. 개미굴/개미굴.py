import sys
input = sys.stdin.readline

class Node():
    def __init__(self, key):
        self.key = key
        self.children = dict()


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

    def print_trie(self, L, curr_node):
        if L == 0:
            curr_node = self.head
        for child in sorted(curr_node.children.keys()):
            print("--" * L, child, sep="")
            self.print_trie(L + 1, curr_node.children[child])


trie = Trie()
n = int(sys.stdin.readline())
for _ in range(n):
    temp = list(sys.stdin.readline().split())
    trie.insert(temp[1:])
trie.print_trie(0, None)