class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        val = []
        dist = []
        res = []
        mindistance =None
        for i in points:
            distance = (i[0]**2) + (i[1]**2)
            dist.append(distance)
            val.append(i)
        index =[]
        minval1 = 0
        for _ in range(k):
            minval1 = min(dist)
            min_index = dist.index(minval1)
            res.append(val[min_index])  
            dist[min_index] = float('inf') #Setting the index as infinity to mark as used
                
        return res
    
solution = Solution()
print(solution.kClosest(points = [[1,3],[-2,2]], k = 1))