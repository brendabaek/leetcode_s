## https://leetcode.com/problems/generate-tag-for-video-caption/

class Solution:
    def generateTag(self, caption: str) -> str:
        lst = caption.title().split()
        if lst == []: return "#"
        return ("#" + lst[0].lower() + "".join(lst[1:]))[:100]