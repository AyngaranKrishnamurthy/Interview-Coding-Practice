class Solution:
    def numSplits(self, s: str) -> int:
        left_list =[]
        right_list=list(s)
        counter = 0
        length = len(right_list)

        while right_list:
            element = right_list.pop(0)
            left_list.append(element)
            left = set(left_list)
            right = set(right_list)
            if len(left) == len(right):
                counter+=1
                
        return counter
		