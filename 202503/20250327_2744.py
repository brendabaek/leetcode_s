## https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        idx, ans, ln = 0, 0, len(words)
        while idx < ln-1 :
            l = words[idx][::-1]
            for i in range(idx+1, ln) :
                if l == words[i] :
                    ans += 1
                    ln -= 1
                    words.pop(i)
                    break
            idx += 1
        return ans