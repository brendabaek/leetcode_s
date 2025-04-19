## https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ln, ans = len(words), 0
        for i in range(ln-1):
            w1, l1 = words[i], len(words[i])
            for j in range(i+1, ln):
                if w1 == words[j][:l1] and w1 == words[j][-l1:]: ans += 1
        return ans