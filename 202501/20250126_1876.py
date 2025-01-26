## https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ln, ans = len(s), 0
        if ln < 3 : return 0
        lst = [s[0], s[1]]
        for i in range(2, ln) :
            lst.append(s[i])
            if lst[0] != lst[1] and lst[1] != lst[2] and lst[0] != lst[2] : ans += 1
            lst.pop(0)
        return ans