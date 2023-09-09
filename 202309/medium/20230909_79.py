## https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        dics = {}
        for boa in board :
            for b in boa :
                try : dics[b] += 1
                except : dics[b] = 1
        
        w_dics = {}
        for w in word :
            try : w_dics[w] += 1
            except : w_dics[w] = 1
        
        print(dics, w_dics)
        for w in w_dics.keys() :
            try :
                if dics[w] < w_dics[w] : return False
            except : return False

        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if board[i][j] == word[0] :
                    if self.check_ans(i, j, 0, board, word) :
                        return True
        return False
        
    def check_ans(self, i, j, cnt, board, word) :
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or cnt >= len(word) \
            or cnt >= len(word) or board[i][j] != word[cnt] : return False
        if cnt == len(word)-1 : return True

        tmp, board[i][j] = board[i][j], 0
        if self.check_ans(i-1, j, cnt+1, board, word) : return True
        if self.check_ans(i+1, j, cnt+1, board, word) : return True
        if self.check_ans(i, j-1, cnt+1, board, word) : return True
        if self.check_ans(i, j+1, cnt+1, board, word) : return True
        board[i][j] = tmp
        return False