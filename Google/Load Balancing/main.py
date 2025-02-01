load = [1, 2, 3, 4, 5]
class Solution(object):
    def loadDifference(self, load: list[int]) -> int: 
        res = 0
        res1=0
        res2=0
        list1=[]
        list2=[]
        load.sort(reverse=True)
        for i in load:
            if res1 <= res2:
                list1.append(i)
                res1 +=i
            else:
                list2.append(i)
                res2+=i
        res = abs(res2-res1)
        
        return res
solution=Solution()
print(solution.loadDifference(load))
