## https://leetcode.com/problems/fair-candy-swap/

class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        s_a, s_b = set(aliceSizes), set(bobSizes)
        find = (sum(aliceSizes) - sum(bobSizes)) / 2
        for num in s_a :
            if num - find in s_b : return [num, num-find]