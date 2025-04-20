## https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        s, ans = sum(apple), 0
        for c in capacity:
            s -= c; ans += 1
            if s <= 0: break
        return ans