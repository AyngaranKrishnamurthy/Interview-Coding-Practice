from collections import Counter
rooms = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]

class Solution(object):
    def maxBooking(self, load: list[str]) -> str:
        list1 =[]
        list2 = []
        for i in rooms:
            list1 = list(i)
            if list1[0] == "+":
                strval = list1[1]+list1[2]
                list2.append(strval)

        counter = Counter(list2)
        res = counter.most_common(1)[0]
        return res
    
solution = Solution()
print(solution.maxBooking(rooms))
