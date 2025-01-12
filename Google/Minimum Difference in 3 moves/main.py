class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 4:  # Special case where we can remove up to 3 elements
            return 0

        nums.sort()  # Sort the list first
        
        # We need to compare the result after removing 0, 1, 2, or 3 largest or smallest elements
        # 4 possible ways to minimize the difference:
        # Remove 3 smallest, 2 smallest + 1 largest, 1 smallest + 2 largest, 3 largest
        return min(
            nums[-4] - nums[0],     # Remove 3 smallest
            nums[-3] - nums[1],     # Remove 2 smallest + 1 largest
            nums[-2] - nums[2],     # Remove 1 smallest + 2 largest
            nums[-1] - nums[3]      # Remove 3 largest
        )
