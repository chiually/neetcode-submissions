class Node:
    def __init__(self):
        self.children = {} # letter to node
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:

        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()

            node = node.children[c]

        # mark as end of word
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False

            node = node.children[c]

        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for c in prefix:
            if c not in node.children:
                return False

            node = node.children[c]

        return True
        
        