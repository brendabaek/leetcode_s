## https://leetcode.com/problems/slowest-key/

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        idx, pre, key, time = 0, 0, 0, 0
        for r in releaseTimes :
            if r - pre > time :
                key, time = keysPressed[idx], r - pre
            if r - pre == time :
                key = max(key, keysPressed[idx])
            idx += 1; pre = r
        return key