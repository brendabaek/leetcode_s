## https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces :
            ln = len(piece)
            try : idx = arr.index(piece[0])
            except : return False
            if piece != arr[idx:idx+ln] : return False
        return True