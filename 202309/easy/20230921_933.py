## https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter(object):
    def __init__(self):
        self.RecentCounter = None
        self.ans = []
        
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.ans.append(t)
        while self.ans[0] < t-3000 : self.ans.pop(0)
        return len(self.ans)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)