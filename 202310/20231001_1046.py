## https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1 :
            max_1 = stones.pop(stones.index(max(stones)))
            max_2 = stones.pop(stones.index(max(stones)))
            if max_1 > max_2 : stones.append(max_1-max_2)
        return sum(stones)