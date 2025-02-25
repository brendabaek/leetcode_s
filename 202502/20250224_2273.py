## https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        idx = 0
        while idx < len(words)-1 :
            nxt = words[idx+1]
            for w in words[idx] :
                if w in nxt : nxt = nxt.replace(w, "", 1)
                else : nxt = "failed"; break
            if nxt == "" : words.pop(idx+1)
            else : idx += 1
        return words