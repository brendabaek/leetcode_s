## https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r, l, b = 0, 0, 0
        for move in moves :
            if move == "R" : r += 1
            elif move == "L" : l += 1
            else : b += 1
        return abs(r - l) + b