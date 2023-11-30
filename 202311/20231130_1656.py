## https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:
    def __init__(self, n: int):
        self.max_num = n+1
        self.dics = {i+1:None for i in range(n)}
        self.stt = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dics[idKey] = value
        ans = []
        for i in range(self.stt, self.max_num) :
            if self.dics[i] != None :
                ans.append(self.dics[i])
            else : self.stt = i; break
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)