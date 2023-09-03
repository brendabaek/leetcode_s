## https://leetcode.com/problems/design-hashset/

class MyHashSet(object):
    def __init__(self):
        self.hash_set = set()
        
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash_set.add(key)
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        try : self.hash_set.remove(key)
        except : pass
        
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.hash_set : return True
        else : return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)