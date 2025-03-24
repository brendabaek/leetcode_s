## https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        idx, cnt, ans = 1, 1, [i for i in range(2, n+1)]
        while True :
            idx = (idx + (cnt * k)) % n
            if idx == 0 : idx = n
            if idx not in ans : return ans
            else : ans.remove(idx); cnt += 1