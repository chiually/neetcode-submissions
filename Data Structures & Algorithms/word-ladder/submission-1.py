from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # make the graph
        adj = {w : [] for w in wordList}
        adj[beginWord] = []
        for w in adj:
            for t in adj:
                if w != t and self.canTransform(w, t):
                    adj[w].append(t)

        # do bfs and return length of path
        if endWord not in adj:
            return 0
        print(adj)
        q = deque([beginWord])

        transformations = 0
        visit = set()
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return transformations + 1
                visit.add(word)

                for nei in adj[word]:
                    if nei in visit:
                        continue
                    q.append(nei)
                    
            transformations += 1

        return 0


    def canTransform(self, w1: str, w2: str):

        count = 0
        i = 0
        while count <= 1 and i < len(w1):
            if w1[i] != w2[i]:
                count += 1
            i += 1

        return True if count < 2 else False
