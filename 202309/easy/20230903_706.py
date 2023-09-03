## https://leetcode.com/problems/design-hashmap/

class MyHashMap(object):

    def __init__(self):
        self.hash_map = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hash_map[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try : return self.hash_map[key]
        except : return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        try : self.hash_map.pop(key)
        except : pass

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)