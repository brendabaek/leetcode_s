## https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        idx, c = 1, groups[0]
        while idx < len(groups) :
            if c == 0 :
                if groups[idx] == 1 : c = 1; idx += 1
                else : words.pop(idx); groups.pop(idx)
            else :
                if groups[idx] == 0 : c = 0; idx += 1
                else : words.pop(idx); groups.pop(idx)
        return words