## https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

import re

class Solution:
    def maxDepth(self, s: str) -> int:
        st = re.sub(r'[^()]', '', s)
        while ")(" in st : st = st.replace(")(", "")
        return len(st)//2