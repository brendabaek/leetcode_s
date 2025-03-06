## https://leetcode.com/problems/count-days-spent-together/

days = {"01":0, "02":31, "03":59, "04":90, "05":120, "06":151, "07":181, "08":212, "09":243, "10":273, "11":304, "12":334}
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        if leaveAlice > leaveBob : arriveAlice, leaveAlice, arriveBob, leaveBob = arriveBob, leaveBob, arriveAlice, leaveAlice
        if arriveBob > leaveAlice : return 0
        elif arriveBob == leaveAlice : return 1
        elif arriveBob <= arriveAlice : return days[leaveAlice[:2]] + int(leaveAlice[3:]) - days[arriveAlice[:2]] - int(arriveAlice[3:]) + 1
        else : return days[leaveAlice[:2]] + int(leaveAlice[3:]) - days[arriveBob[:2]] - int(arriveBob[3:]) + 1