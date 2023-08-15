## https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board :
            tmp = [r for r in row if r != '.']
            if self.answer(tmp) == False : return False

        for i in range(9) :
            tmp = []
            for j in range(9) :
                if board[j][i] != '.' :
                    tmp.append(board[j][i])
            if self.answer(tmp) == False : return False

        for i in range(3) :
            for j in range(3) :
                tmp = []
                for k in range(3) :
                    k = (i*3) + k
                    for l in range(3) :
                        l = (j*3) + l
                        if board[k][l] != '.' :
                            tmp.append(board[k][l])
                if self.answer(tmp) == False : return False
        return True

    def answer(self, tmp) :
        tmp.sort()
        c = 0
        for t in tmp :
            if t == c : return False
            c = t
        return True