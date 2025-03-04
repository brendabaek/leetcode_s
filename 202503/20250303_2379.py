## https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ln, m = len(blocks), 0
        for i in range(ln-k+1) : m = max(m, blocks[i:i+k].count("B"))
        return k - m