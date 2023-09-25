## https://leetcode.com/problems/available-captures-for-rook/

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ln_r, ln_c, ans = len(board), len(board[0]), 0
        for i in range(ln_r) :
            try : r, c = i, board[i].index("R")
            except : pass

        cnt = c - 1
        while cnt > -1 :
            if board[r][cnt] == '.' : cnt -= 1
            else :
                if board[r][cnt] == 'p' : ans += 1
                break

        cnt = c + 1
        while cnt < ln_c :
            if board[r][cnt] == '.' : cnt += 1
            else :
                if board[r][cnt] == 'p' : ans += 1
                break

        cnt = r - 1
        while cnt > -1 :
            if board[cnt][c] == '.' : cnt -= 1
            else :
                if board[cnt][c] == 'p' : ans += 1
                break

        cnt = r + 1
        while cnt < ln_r :
            if board[cnt][c] == '.' : cnt += 1
            else :
                if board[cnt][c] == 'p' : ans += 1
                break

        return ans