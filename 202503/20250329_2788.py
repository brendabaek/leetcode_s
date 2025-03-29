## https://leetcode.com/problems/split-strings-by-separator/

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [w for word in words for w in word.split(separator) if w]

        # ans = []
        # for word in words : 
        #     for w in word.split(separator) :
        #         if w : ans.append(w)
        # return ans

        # ans = []
        # for word in words : ans += word.strip(separator).split(separator)
        # ans = [a for a in ans if a != ""]
        # return ans