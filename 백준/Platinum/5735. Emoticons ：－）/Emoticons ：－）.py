from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.trie = defaultdict(dict)
        self.output = defaultdict(list)
        self.fail = defaultdict(lambda: 0)
        self.num_nodes = 0
    
    def insert(self, word, index):
        node = 0
        for char in word:
            if char not in self.trie[node]:
                self.num_nodes += 1
                self.trie[node][char] = self.num_nodes
            node = self.trie[node][char]
        self.output[node].append((index, word))
    
    def build_failure_links(self):
        queue = deque()
        for char in self.trie[0]:
            child = self.trie[0][char]
            queue.append(child)
            self.fail[child] = 0
        
        while queue:
            current = queue.popleft()
            for char in self.trie[current]:
                child = self.trie[current][char]
                fail_state = self.fail[current]
                
                while fail_state > 0 and char not in self.trie[fail_state]:
                    fail_state = self.fail[fail_state]
                
                if char in self.trie[fail_state]:
                    self.fail[child] = self.trie[fail_state][char]
                else:
                    self.fail[child] = 0
                
                self.output[child].extend(self.output[self.fail[child]])
from collections import deque, defaultdict

class TrieNode:
    def __init__(self):
        self.prefix = ""
        self.is_end = False
        self.children = {}
        self.fail_link = None

class AhoCorasick:
    def __init__(self):
        self.root = TrieNode()

    def insert_pattern(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.prefix = pattern
        node.is_end = True

    def build_failure_links(self):
        root = self.root
        queue = deque([root])

        while queue:
            current_node = queue.popleft()

            for char, child_node in current_node.children.items():
                if current_node == root:
                    child_node.fail_link = root
                else:
                    fail_node = current_node.fail_link
                    while fail_node != root and char not in fail_node.children:
                        fail_node = fail_node.fail_link
                    
                    if char in fail_node.children:
                        fail_node = fail_node.children[char]
                    
                    child_node.fail_link = fail_node
                
                if child_node.fail_link.is_end:
                    child_node.is_end = True

                queue.append(child_node)

    def search_in_text(self, text):
        node = self.root
        result = 0

        for char in text:
            while node != self.root and char not in node.children:
                node = node.fail_link

            if char in node.children:
                node = node.children[char]

            if node.is_end:
                result += 1
                node = self.root

        return result

def find_answer(N, M):
    ac = AhoCorasick()

   
    for _ in range(N):
        pattern = input().strip()
        ac.insert_pattern(pattern)

  
    ac.build_failure_links()

    total_count = 0

 
    for _ in range(M):
        text = input().strip()
        total_count += ac.search_in_text(text)

    print(total_count)

def main():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        find_answer(N, M)

if __name__ == "__main__":
    main()