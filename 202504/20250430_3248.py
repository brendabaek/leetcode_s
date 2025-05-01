## https://leetcode.com/problems/snake-in-matrix/

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        p1, p2 = 0, 0
        for c in commands:
            if c == "DOWN": p1 += 1
            elif c == "UP": p1 -= 1
            elif c == "RIGHT": p2 += 1
            elif c == "LEFT": p2 -= 1            
        return (p1 * n) + p2