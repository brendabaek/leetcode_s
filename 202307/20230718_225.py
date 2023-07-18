## https://leetcode.com/problems/implement-stack-using-queues/

class MyStack(object):
    def __init__(self):
        self.lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.lst.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.lst.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.lst[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.lst) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()