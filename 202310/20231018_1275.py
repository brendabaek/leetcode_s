## https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5 : return 'Pending'
        base = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        p = 'A'
        ans = [['A', 'A', 'A'], ['B', 'B', 'B']]
        
        for m in moves :
            base[m[0]][m[1]] = p
            for i in range(3) :
                if base[i] in ans : return p
                elif [base[0][i], base[1][i], base[2][i]] in ans : return p
                elif [base[0][0], base[1][1], base[2][2]] in ans : return p
                elif [base[0][2], base[1][1], base[2][0]] in ans : return p
            if not (0 in base[0] or 0 in base[1] or 0 in base[2]) : return 'Draw'
            if p == 'A' : p = 'B'
            else : p = 'A'
        return 'Pending'