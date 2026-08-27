class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            # sort the string to make any anagrams the same
            # note that strings are hashable
            sorted_s = "".join(sorted(s))

            curr_list = anagrams.get(sorted_s, [])
            curr_list.append(s)
            anagrams[sorted_s] = curr_list

        return list(anagrams.values())
        