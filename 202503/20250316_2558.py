## https://leetcode.com/problems/take-gifts-from-the-richest-pile/

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        tmp = []
        for _ in range(k) :
            if gifts == [] :
                gifts = tmp
                gifts.sort()
                tmp = []
                tmp.append(int(gifts.pop() ** 0.5))
            elif tmp == [] :
                tmp.append(int(gifts.pop() ** 0.5))
            elif tmp[0] < gifts[-1]:
                tmp.append(int(gifts.pop() ** 0.5))
            else :
                gifts = gifts + tmp
                gifts.sort()
                tmp = []
                tmp.append(int(gifts.pop() ** 0.5))
        return sum(gifts) + sum(tmp)