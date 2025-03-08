## https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sums, cnt = 0, 0
        for num in nums :
            if num % 6 == 0 : sums, cnt = sums + num, cnt + 1
        return 0 if cnt == 0 else sums // cnt