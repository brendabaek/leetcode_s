## https://leetcode.com/problems/reformat-date/

month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06",
        "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
class Solution:
    def reformatDate(self, date: str) -> str:
        lst = date.split(" ")
        ans = lst[2] + '-' + month[lst[1]] + '-'
        if len(lst[0]) == 3 : return ans + "0" + lst[0][0]
        else : return ans + lst[0][:2]