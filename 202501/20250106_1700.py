## https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        while True :
            for i in range(n) :
                if students[0] == sandwiches[0] :
                    students.pop(0)
                    sandwiches.pop(0)
                else : students.append(students.pop(0))
            new_n = len(students)
            if new_n == 0 or n == new_n : return new_n
            else : n = new_n