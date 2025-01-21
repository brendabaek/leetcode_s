## https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return False if (ord(coordinates[0]) + int(coordinates[1])) % 2 == 0 else True