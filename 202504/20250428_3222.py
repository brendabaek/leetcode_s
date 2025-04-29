## https://leetcode.com/problems/find-the-winning-player-in-coin-game/

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        ans = 0
        while x >= 1 and y >= 4: x -= 1; y -= 4; ans += 1
        return "Alice" if ans % 2 == 1 else "Bob"