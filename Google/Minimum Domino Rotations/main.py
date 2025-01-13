from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(val):
            tops_rotation=bottoms_rotation=0
            for i in range(len(tops)):
                if tops[i]!=val and bottoms[i]!=val:
                    return -1
                elif tops[i] != val:
                    tops_rotation+=1
                elif bottoms[i]!= val:
                    bottoms_rotation+=1
            return min(tops_rotation,bottoms_rotation)
        
        rotations = check(tops[0])
        if rotations != -1:
            return rotations
        else:
            return check(bottoms[0])
    
        
