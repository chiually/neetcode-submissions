class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # intialize graph
        adj = {c : set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # check if word id prefix and if valid ordering
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # build graph
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {} # False=visited True=in curr path
        res = []

        def dfs(c):
            if c in visited:
                return visited[c] # True when loop found

            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)

