## https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ln, ans = len(words), 0
        lst = [set() for _ in range(ln)]
        for i in range(ln) :
            for w in words[i] : lst[i].add(w)
        for j in range(ln-1) :
            for k in range(j+1, ln) :
                if lst[j] == lst[k] : ans += 1
        return ans

        # ans, ln = 0, len(words)
        # for i in range(ln-1) :
        #     for j in range(i+1, ln) :
        #         if set(words[i]) == set(words[j]) : ans += 1
        # return ans