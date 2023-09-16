## https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        l1, l2, ans = s1.split(" "), s2.split(" "), []
        while len(l1) > 0 :
            word = l1[0]
            cnt1, cnt2 = l1.count(word), l2.count(word)
            if cnt1 + cnt2 == 1 : ans.append(word)
            for _ in range(cnt1) : l1.remove(word)
            for _ in range(cnt2) : l2.remove(word)
        while len(l2) > 0 :
            word = l2[0]
            cnt2 = l2.count(word)
            if cnt2 == 1 : ans.append(word)
            for _ in range(cnt2) : l2.remove(word)
        return ans