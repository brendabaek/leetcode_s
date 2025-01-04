## https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        allowed = set(allowed)
        for word in words :
            cnt += 1
            for w in word :
                if w not in allowed :
                    cnt -= 1
                    break
        return cnt