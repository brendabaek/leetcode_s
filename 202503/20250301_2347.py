## https://leetcode.com/problems/best-poker-hand/

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1 : return "Flush"
        dics = {}
        for rank in ranks :
            try : dics[rank] += 1
            except : dics[rank] = 1
        if 4 in dics.values() : return "Three of a Kind"
        elif 3 in dics.values() : return "Three of a Kind"
        elif 2 in dics.values() : return "Pair"
        else : return "High Card"