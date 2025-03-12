## https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words : return -1
        idx, ln, lst, ans = 0, len(words), [], len(words)
        while idx < ln :
            if words[idx] == target : lst.append(idx)
            idx += 1
        for l in lst :
            ans = min(ans, abs(l-startIndex), abs(l + ln - startIndex), abs(l - ln - startIndex))
        return ans