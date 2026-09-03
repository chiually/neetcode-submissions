class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # make the prefix tree
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res = set() # use set to avoid duplicates

        def dfs(i, j, tree, word):

            # check the bounds of i and j
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] not in tree.children:
                return

            # build the current word
            c = board[i][j]
            node = tree.children[c]
            word += c
            if node.endOfWord: # need to check child node since that actually holds the letter
                res.add(word)

            # mark curr position as visited
            board[i][j] = '*'

            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)

            board[i][j] = c # backtrack

        # for each cell on the board, run dfs
        for x in range(ROWS):
            for y in range(COLS):
                dfs(x, y, root, "")
                
        return list(res)

        