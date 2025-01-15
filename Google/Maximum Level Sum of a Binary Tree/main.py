# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int: # type: ignore
        queue = [root]
        max_sum = root.val
        max_level = 1
        current_level = 1

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    level_sum += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level 
            current_level += 1   

        res = max_level
        return res
        
root = [1,7,0,7,-8,null,null] #type: ignore
solution = Solution()
val = solution.maxLevelSum(root)
        