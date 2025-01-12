class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 4:  
            return 0

        nums.sort()

        return min(
            nums[-4] - nums[0],     # Remove 3 smallest
            nums[-3] - nums[1],     # Remove 2 smallest + 1 largest
            nums[-2] - nums[2],     # Remove 1 smallest + 2 largest
            nums[-1] - nums[3]      # Remove 3 largest
        )

nums = [0,0,1,5,0,6,6,6,4,6,4]

solution = Solution()
print(solution.minDifference(nums))
