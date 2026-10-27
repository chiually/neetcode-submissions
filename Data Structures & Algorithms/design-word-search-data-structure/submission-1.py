class TrieNode:
    def __init__(self):
        self.children = {} # char : TrieNode
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]        

        node.endOfWord = True


    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.endOfWord

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
            elif word[i] in node.children:
                return dfs(i + 1, node.children[word[i]])

            return False

        return dfs(0, self.root)
        
