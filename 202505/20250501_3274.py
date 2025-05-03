## https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return True if (ord(coordinate1[0]) + int(coordinate1[1])) % 2 == (ord(coordinate2[0]) + int(coordinate2[1])) % 2 else False