## https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        # score1, score2 = self.score(player1), self.score(player2)
        if score1 > score2 : return 1
        elif score1 < score2 : return 2
        return 0
    
    # def score(self, player) :
    #     p1, p2, ans, idx, ln = 0, 0, 0, 0, len(player)
    #     while idx < ln :
    #         if p1 == 10 or p2 == 10 : ans += 2 * player[idx]
    #         else : ans += player[idx]
    #         p1, p2, idx = p2, player[idx], idx + 1
    #     return ans